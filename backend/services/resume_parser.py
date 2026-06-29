"""
Resume Parser Service
Extracts a CandidateProfile from an uploaded PDF or DOCX file.
Uses heuristics + keyword matching — no external API needed.
"""

from __future__ import annotations
import re
import uuid
import os
from typing import List, Optional

from core.models import CandidateProfile, WorkExperience, Education, ActivitySignals

# ── Large skill vocabulary for keyword extraction ─────────────
SKILL_VOCAB = {
    # Languages
    "python", "java", "javascript", "typescript", "c++", "c#", "go", "rust",
    "ruby", "php", "swift", "kotlin", "scala", "r", "matlab", "perl", "bash",
    "shell", "sql", "html", "css", "dart", "elixir", "haskell",
    # Frameworks & Libraries
    "react", "vue", "angular", "svelte", "next.js", "nuxt", "django", "flask",
    "fastapi", "spring", "express", "rails", "laravel", "tensorflow", "pytorch",
    "keras", "scikit-learn", "pandas", "numpy", "scipy", "huggingface",
    "transformers", "langchain", "openai", "xgboost", "lightgbm", "catboost",
    "opencv", "nltk", "spacy", "gensim",
    # Cloud & DevOps
    "aws", "gcp", "azure", "docker", "kubernetes", "terraform", "ansible",
    "jenkins", "github actions", "circleci", "helm", "prometheus", "grafana",
    "airflow", "kafka", "rabbitmq", "redis", "nginx", "linux",
    # Databases
    "postgresql", "mysql", "mongodb", "sqlite", "elasticsearch", "cassandra",
    "dynamodb", "firestore", "neo4j", "bigquery", "snowflake", "dbt",
    # ML / AI
    "machine learning", "deep learning", "nlp", "computer vision", "llm",
    "rag", "fine-tuning", "embedding", "faiss", "vector database", "mlops",
    "mlflow", "wandb", "data science", "feature engineering", "a/b testing",
    # Tools
    "git", "jira", "confluence", "figma", "postman", "graphql", "rest api",
    "microservices", "ci/cd", "agile", "scrum",
}

DEGREE_KEYWORDS = {
    "b.tech", "b.e.", "be", "btech", "bachelor", "b.sc", "bsc",
    "m.tech", "mtech", "m.sc", "msc", "master", "mba",
    "ph.d", "phd", "doctorate",
}

SENIORITY_BY_YEARS = {
    (0, 2): "junior",
    (2, 5): "mid",
    (5, 9): "senior",
    (9, 99): "lead",
}


# ── Text Extraction ───────────────────────────────────────────

def extract_text_from_pdf(filepath: str) -> str:
    """Extract raw text from a PDF file using pdfplumber."""
    try:
        import pdfplumber
        text_parts = []
        with pdfplumber.open(filepath) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    text_parts.append(t)
        return "\n".join(text_parts)
    except Exception as e:
        print(f"[ResumeParser] PDF extraction error: {e}")
        return ""


def extract_text_from_docx(filepath: str) -> str:
    """Extract raw text from a .docx file using python-docx."""
    try:
        from docx import Document
        doc = Document(filepath)
        return "\n".join(para.text for para in doc.paragraphs if para.text.strip())
    except Exception as e:
        print(f"[ResumeParser] DOCX extraction error: {e}")
        return ""


def extract_text(filepath: str) -> str:
    ext = os.path.splitext(filepath)[1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(filepath)
    elif ext in (".doc", ".docx"):
        return extract_text_from_docx(filepath)
    return ""


# ── NLP Heuristics ────────────────────────────────────────────

def extract_name(lines: List[str]) -> str:
    """
    Heuristic: the candidate's name is usually on the first 1-3 non-empty lines.
    Pick the first line that looks like a proper name (2-4 words, all capitalized,
    no digits or @).
    """
    for line in lines[:8]:
        line = line.strip()
        if not line or "@" in line or any(c.isdigit() for c in line):
            continue
        words = line.split()
        if 2 <= len(words) <= 4 and all(w[0].isupper() for w in words if w):
            return line
    # Fallback: return first non-empty line
    return next((l.strip() for l in lines if l.strip()), "Unknown Candidate")


def extract_skills(text: str) -> List[str]:
    """Match text against skill vocabulary (case-insensitive)."""
    text_lower = text.lower()
    found = []
    for skill in SKILL_VOCAB:
        # Word-boundary match to avoid partial hits
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
            found.append(skill.title() if len(skill.split()) == 1 else skill)
    return sorted(set(found))


def extract_experience_years(text: str) -> float:
    """
    Look for patterns like '5 years', '5+ years', '3-5 years experience'.
    Returns the highest number found (likely total experience).
    """
    patterns = [
        r'(\d+)\+?\s*years?\s+of\s+experience',
        r'(\d+)\+?\s*years?\s+experience',
        r'experience\s+of\s+(\d+)\+?\s*years?',
        r'(\d+)\+?\s*yrs?\s+(?:of\s+)?(?:experience|exp)',
    ]
    found_years = []
    for pat in patterns:
        matches = re.findall(pat, text, re.IGNORECASE)
        found_years.extend(int(m) for m in matches)

    if found_years:
        return float(max(found_years))

    # Fallback: count distinct year mentions in work history (e.g., 2019 - 2023)
    year_spans = re.findall(r'(20\d{2}|19\d{2})\s*[-–]\s*(20\d{2}|19\d{2}|present)', text, re.IGNORECASE)
    total = 0.0
    for start, end in year_spans:
        try:
            s = int(start)
            e = 2025 if end.lower() == "present" else int(end)
            total += max(0, e - s)
        except ValueError:
            pass
    return min(round(total, 1), 40.0)  # cap at 40 years


def extract_education(text: str) -> List[Education]:
    """Look for degree keywords and capture surrounding context."""
    educations = []
    lines = text.split("\n")
    for i, line in enumerate(lines):
        line_lower = line.lower()
        for deg in DEGREE_KEYWORDS:
            if deg in line_lower:
                # Try to grab institution from same or adjacent lines
                context = " ".join(lines[max(0, i-1):i+2])
                # Extract institution: often "from/at <Institution Name>"
                inst_match = re.search(r'(?:from|at|,)\s+([A-Z][A-Za-z\s&]+)', context)
                institution = inst_match.group(1).strip() if inst_match else ""
                # Normalize degree name
                degree_map = {
                    "b.tech": "B.Tech", "btech": "B.Tech", "b.e.": "B.E.", "be": "B.E.",
                    "bachelor": "Bachelor's", "b.sc": "B.Sc", "bsc": "B.Sc",
                    "m.tech": "M.Tech", "mtech": "M.Tech", "m.sc": "M.Sc", "msc": "M.Sc",
                    "master": "Master's", "mba": "MBA",
                    "ph.d": "Ph.D", "phd": "Ph.D", "doctorate": "Ph.D",
                }
                degree_name = degree_map.get(deg, deg.upper())
                # Extract field from line if possible
                field_match = re.search(
                    r'(?:in|of)\s+([A-Za-z\s]+?)(?:\s+from|\s+at|,|$)', line, re.IGNORECASE
                )
                field = field_match.group(1).strip() if field_match else ""
                educations.append(Education(
                    degree=degree_name, field=field, institution=institution
                ))
                break  # one match per line
    return educations[:3]  # cap at 3


def extract_summary(text: str) -> str:
    """
    Find a summary/objective section or use the first substantial paragraph.
    """
    # Try to find explicit section
    summary_match = re.search(
        r'(?:summary|objective|profile|about me)[:\s]*\n(.+?)(?:\n\n|\n[A-Z]{3,})',
        text, re.IGNORECASE | re.DOTALL
    )
    if summary_match:
        return summary_match.group(1).strip()[:500]

    # Fallback: first paragraph with >= 30 words
    paragraphs = [p.strip() for p in text.split("\n\n") if len(p.split()) >= 30]
    return paragraphs[0][:500] if paragraphs else ""


def infer_seniority(years: float) -> str:
    for (lo, hi), level in SENIORITY_BY_YEARS.items():
        if lo <= years < hi:
            return level
    return "senior"


def extract_headline(lines: List[str], name: str) -> str:
    """
    Headline is usually the 2nd line after the name (title/role).
    """
    name_found = False
    for line in lines[:10]:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped == name:
            name_found = True
            continue
        if name_found:
            # Skip if it looks like contact info
            if "@" in stripped or re.match(r'[\d\+\(\)]+', stripped):
                continue
            if len(stripped.split()) <= 8:
                return stripped
    return ""


# ── Main Parser ───────────────────────────────────────────────

def parse_resume_to_candidate(filepath: str, filename: str) -> Optional[CandidateProfile]:
    """
    Full pipeline: extract text → run all heuristics → return CandidateProfile.
    Returns None if text extraction fails.
    """
    text = extract_text(filepath)
    if not text or len(text.strip()) < 50:
        return None

    lines = [l for l in text.split("\n") if l.strip()]

    name = extract_name(lines)
    headline = extract_headline(lines, name)
    skills = extract_skills(text)
    exp_years = extract_experience_years(text)
    education = extract_education(text)
    summary = extract_summary(text)
    seniority = infer_seniority(exp_years)

    candidate_id = f"upload_{uuid.uuid4().hex[:8]}"

    print(f"[ResumeParser] Parsed '{filename}': {name}, {exp_years}y exp, {len(skills)} skills")

    return CandidateProfile(
        candidate_id=candidate_id,
        name=name,
        headline=headline or f"Uploaded from {filename}",
        summary=summary,
        skills=skills[:20],  # top 20 matched skills
        total_experience_years=exp_years,
        education=education,
        work_history=[],
        activity=ActivitySignals(
            github_active=False,
            open_source_contributions=0,
            blog_posts=0,
            last_active_days_ago=7,  # fresh upload = recently active
            certifications_recent=0,
        ),
        location="",
        expected_role_level=seniority,
        source="uploaded",
    )
