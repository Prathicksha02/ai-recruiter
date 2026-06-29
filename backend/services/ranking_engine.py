"""
Ranking Engine — the core AI brain.

5-Signal Weighted Scoring:
  1. Semantic Similarity   (40%) — embedding cosine similarity
  2. Skills Match          (25%) — keyword overlap with JD required skills
  3. Experience Fit        (20%) — how well years of experience matches JD range
  4. Activity Score        (10%) — GitHub, blogs, certifications, recency
  5. Seniority Fit          (5%) — role level alignment

Final Score → Grade → AI Reasoning (human-readable)
"""

from __future__ import annotations
import numpy as np
from typing import List
from core.models import (
    CandidateProfile, JobDescription,
    RankedCandidate, SignalBreakdown
)
from services.embedding_service import (
    candidate_to_text, jd_to_text, embed_texts, cosine_similarity
)

WEIGHTS = {
    "semantic":    0.40,
    "skills":      0.25,
    "experience":  0.20,
    "activity":    0.10,
    "seniority":   0.05,
}

SENIORITY_MAP = {"junior": 1, "mid": 2, "senior": 3, "lead": 4}

# ── Signal Scorers ────────────────────────────────────────────

def score_semantic(jd_vec: np.ndarray, cand_vec: np.ndarray) -> float:
    sim = cosine_similarity(jd_vec, cand_vec)
    # Normalize from [-1,1] to [0,100]
    return round(((sim + 1) / 2) * 100, 2)

def score_skills(jd: JobDescription, candidate: CandidateProfile) -> float:
    if not jd.required_skills:
        return 60.0  # neutral if no skills specified
    candidate_skills_lower = {s.lower() for s in candidate.skills}
    required_lower = [s.lower() for s in jd.required_skills]
    matches = sum(1 for s in required_lower if s in candidate_skills_lower)
    # Partial credit for preferred skills
    preferred_lower = [s.lower() for s in (jd.preferred_skills or [])]
    pref_matches = sum(1 for s in preferred_lower if s in candidate_skills_lower)
    base = (matches / len(required_lower)) * 85
    bonus = min(15, (pref_matches / max(len(preferred_lower), 1)) * 15)
    return round(min(100, base + bonus), 2)

def score_experience(jd: JobDescription, candidate: CandidateProfile) -> float:
    exp = candidate.total_experience_years
    min_exp = jd.min_experience_years or 0
    max_exp = jd.max_experience_years or 20
    if exp < min_exp:
        # Under-experienced — penalize proportionally
        gap = min_exp - exp
        return round(max(0, 100 - gap * 15), 2)
    elif exp > max_exp + 3:
        # Over-qualified — slight penalty
        return round(max(60, 100 - (exp - max_exp) * 5), 2)
    else:
        # In sweet spot
        mid = (min_exp + max_exp) / 2
        distance = abs(exp - mid) / max((max_exp - min_exp) / 2, 1)
        return round(max(75, 100 - distance * 20), 2)

def score_activity(candidate: CandidateProfile) -> float:
    a = candidate.activity
    if not a:
        return 40.0
    score = 40.0
    if a.github_active:
        score += 15
    contrib_score = min(20, a.open_source_contributions * 0.5)
    score += contrib_score
    blog_score = min(10, a.blog_posts * 1.5)
    score += blog_score
    cert_score = min(10, a.certifications_recent * 3)
    score += cert_score
    # Recency bonus: active in last 14 days
    if a.last_active_days_ago <= 14:
        score += 5
    elif a.last_active_days_ago > 90:
        score -= 10
    return round(min(100, max(0, score)), 2)

def score_seniority(jd: JobDescription, candidate: CandidateProfile) -> float:
    jd_level = SENIORITY_MAP.get(jd.seniority_level or "mid", 2)
    cand_level = SENIORITY_MAP.get(candidate.expected_role_level or "mid", 2)
    diff = abs(jd_level - cand_level)
    return round({0: 100, 1: 70, 2: 40, 3: 10}.get(diff, 10), 2)

# ── Grade & Reasoning ─────────────────────────────────────────

def compute_grade(score: float) -> str:
    if score >= 88: return "A+"
    if score >= 78: return "A"
    if score >= 68: return "B+"
    if score >= 55: return "B"
    return "C"

def generate_reasoning(
    candidate: CandidateProfile, jd: JobDescription,
    signals: SignalBreakdown, final_score: float
) -> str:
    parts = []
    if signals.semantic_similarity >= 75:
        parts.append(f"Strong semantic alignment with the {jd.title} role")
    elif signals.semantic_similarity >= 55:
        parts.append(f"Moderate semantic fit for {jd.title}")
    else:
        parts.append(f"Limited semantic overlap with {jd.title}")

    if signals.skills_match >= 80:
        parts.append(f"covers most required skills well")
    elif signals.skills_match >= 55:
        parts.append(f"covers some key skills")
    else:
        parts.append(f"has skill gaps vs requirements")

    exp = candidate.total_experience_years
    parts.append(f"{exp:.0f} years experience ({candidate.expected_role_level}-level)")

    if signals.activity_score >= 70:
        parts.append("highly active in community/open-source")
    elif signals.activity_score <= 40:
        parts.append("low recent activity signals")

    return ". ".join(parts).capitalize() + "."

# ── Main Rank Function ────────────────────────────────────────

def rank_candidates(
    candidates: List[CandidateProfile],
    jd: JobDescription,
    top_k: int = 10
) -> List[RankedCandidate]:

    # 1. Embed JD and all candidates
    jd_text = jd_to_text(jd)
    candidate_texts = [candidate_to_text(c) for c in candidates]
    all_texts = [jd_text] + candidate_texts
    all_vecs = embed_texts(all_texts)
    jd_vec = all_vecs[0]
    cand_vecs = all_vecs[1:]

    results = []
    for i, (candidate, cand_vec) in enumerate(zip(candidates, cand_vecs)):
        sem  = score_semantic(jd_vec, cand_vec)
        skl  = score_skills(jd, candidate)
        exp  = score_experience(jd, candidate)
        act  = score_activity(candidate)
        snr  = score_seniority(jd, candidate)

        final = (
            sem  * WEIGHTS["semantic"] +
            skl  * WEIGHTS["skills"] +
            exp  * WEIGHTS["experience"] +
            act  * WEIGHTS["activity"] +
            snr  * WEIGHTS["seniority"]
        )
        final = round(final, 2)

        signals = SignalBreakdown(
            semantic_similarity=sem,
            skills_match=skl,
            experience_fit=exp,
            activity_score=act,
            seniority_fit=snr
        )
        reasoning = generate_reasoning(candidate, jd, signals, final)
        grade = compute_grade(final)

        results.append(RankedCandidate(
            rank=0,  # filled after sort
            candidate_id=candidate.candidate_id,
            name=candidate.name,
            headline=candidate.headline or "",
            skills=candidate.skills[:8],
            total_experience_years=candidate.total_experience_years,
            location=candidate.location or "",
            final_score=final,
            signals=signals,
            ai_reasoning=reasoning,
            match_grade=grade,
            source=candidate.source or "seed",
        ))

    # Sort descending by final score
    results.sort(key=lambda x: x.final_score, reverse=True)
    for idx, r in enumerate(results[:top_k]):
        r.rank = idx + 1

    return results[:top_k]
