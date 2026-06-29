"""
Embedding Service — converts text to semantic vectors using local sentence-transformers.
Model: all-MiniLM-L6-v2 (fast, lightweight, great quality — downloads once ~80MB)
"""

from __future__ import annotations
import numpy as np
from typing import List
from sentence_transformers import SentenceTransformer
from core.models import CandidateProfile, JobDescription

_model = None

def get_model() -> SentenceTransformer:
    global _model
    if _model is None:
        print("Loading embedding model (first time only)...")
        _model = SentenceTransformer("all-MiniLM-L6-v2")
        print("Model loaded!")
    return _model

def candidate_to_text(c: CandidateProfile) -> str:
    """Converts a candidate profile into a rich text blob for embedding."""
    work = " ".join([
        f"{w.title} at {w.company}: {w.description}"
        for w in c.work_history
    ])
    edu = " ".join([f"{e.degree} in {e.field} from {e.institution}" for e in c.education])
    skills = " ".join(c.skills)
    return f"""
    {c.headline}. {c.summary}
    Skills: {skills}.
    Experience: {work}
    Education: {edu}
    Role level: {c.expected_role_level}. Location: {c.location}.
    """.strip()

def jd_to_text(jd: JobDescription) -> str:
    """Converts a job description into a text blob for embedding."""
    req = " ".join(jd.required_skills or [])
    pref = " ".join(jd.preferred_skills or [])
    return f"""
    {jd.title}. {jd.description}
    Required skills: {req}.
    Preferred skills: {pref}.
    Seniority: {jd.seniority_level}. Domain: {jd.domain}.
    Experience: {jd.min_experience_years} to {jd.max_experience_years} years.
    """.strip()

def embed_texts(texts: List[str]) -> np.ndarray:
    model = get_model()
    return model.encode(texts, normalize_embeddings=True, show_progress_bar=False)

def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """Both vectors are already L2-normalized, so dot product = cosine similarity."""
    return float(np.dot(a, b))
