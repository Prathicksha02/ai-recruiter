"""
FastAPI main entry point — AI Recruiter API
"""
import os
import shutil
import sys
import time

# Force UTF-8 output on Windows terminals
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from core.models import CandidateProfile, RankRequest, RankResponse
from services.ranking_engine import rank_candidates
from services.resume_parser import parse_resume_to_candidate
from services.resume_parser import extract_text_from_pdf
from data.seed_candidates import SEED_CANDIDATES

_candidates: list[CandidateProfile] = []

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {".pdf", ".doc", ".docx"}


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load seed candidates into memory at startup."""
    global _candidates
    _candidates = [CandidateProfile(**c) for c in SEED_CANDIDATES]
    print(f"[OK] Loaded {len(_candidates)} seed candidates into memory.")
    yield
    print("Server shutting down.")


app = FastAPI(title="AI Recruiter API", version="2.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Health & Info ─────────────────────────────────────────────

@app.get("/")
def root():
    seed_count = sum(1 for c in _candidates if c.source == "seed")
    uploaded_count = sum(1 for c in _candidates if c.source == "uploaded")
    return {
        "status": "ok",
        "candidates_loaded": len(_candidates),
        "seed_candidates": seed_count,
        "uploaded_candidates": uploaded_count,
    }


# ── Candidate Endpoints ───────────────────────────────────────

@app.get("/candidates")
def list_candidates():
    return [
        {
            "id": c.candidate_id,
            "name": c.name,
            "headline": c.headline,
            "skills": c.skills[:6],
            "experience": c.total_experience_years,
            "location": c.location,
            "source": c.source,
        }
        for c in _candidates
    ]


@app.get("/candidates/uploaded")
def list_uploaded_candidates():
    """Returns only candidates that were uploaded (not seed data)."""
    return [
        {
            "id": c.candidate_id,
            "name": c.name,
            "headline": c.headline,
            "skills": c.skills[:6],
            "experience": c.total_experience_years,
            "source": c.source,
        }
        for c in _candidates if c.source == "uploaded"
    ]


@app.delete("/candidates/{candidate_id}")
def delete_candidate(candidate_id: str):
    """Remove an uploaded candidate from the pool."""
    global _candidates
    original_count = len(_candidates)
    _candidates = [c for c in _candidates if c.candidate_id != candidate_id]
    if len(_candidates) == original_count:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return {"status": "removed", "total": len(_candidates)}


@app.post("/candidates/add")
def add_candidate(candidate: CandidateProfile):
    """Add a candidate profile manually (JSON)."""
    _candidates.append(candidate)
    return {"status": "added", "total": len(_candidates)}

@app.post("/upload-jd")
async def upload_jd(file: UploadFile = File(...)):
    upload_path = os.path.join("uploads", file.filename)

    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Read text from the uploaded file
    text = ""

    if file.filename.endswith(".txt"):
        with open(upload_path, "r", encoding="utf-8") as f:
            text = f.read()

    elif file.filename.endswith(".pdf"):
        from services.resume_parser import extract_text_from_pdf
        text = extract_text_from_pdf(upload_path)

    elif file.filename.endswith(".docx"):
        from services.resume_parser import extract_text_from_docx
        text = extract_text_from_docx(upload_path)

    return {
        "job_description": text
    }
# ── Resume Upload & Parse ─────────────────────────────────────

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    """
    Upload a PDF or DOCX resume → parse → extract CandidateProfile →
    add to the live ranking pool.
    Returns the extracted candidate data for the frontend to preview.
    """
    ext = os.path.splitext(file.filename or "")[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type '{ext}'. Please upload PDF, DOC, or DOCX."
        )

    # Save file
    safe_name = f"{time.time_ns()}_{file.filename}"
    file_path = os.path.join(UPLOAD_FOLDER, safe_name)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Parse
    candidate = parse_resume_to_candidate(file_path, file.filename or "resume")
    if candidate is None:
        raise HTTPException(
            status_code=422,
            detail="Could not extract text from this file. Make sure it's not a scanned image."
        )

    # Add to live pool
    _candidates.append(candidate)

    seed_count = sum(1 for c in _candidates if c.source == "seed")
    uploaded_count = sum(1 for c in _candidates if c.source == "uploaded")

    return {
        "status": "success",
        "message": f"Resume parsed and added to ranking pool!",
        "candidate": {
            "id": candidate.candidate_id,
            "name": candidate.name,
            "headline": candidate.headline,
            "skills": candidate.skills[:8],
            "experience": candidate.total_experience_years,
            "seniority": candidate.expected_role_level,
            "education": [
                {"degree": e.degree, "field": e.field, "institution": e.institution}
                for e in candidate.education
            ],
        },
        "pool": {
            "total": len(_candidates),
            "seed": seed_count,
            "uploaded": uploaded_count,
        }
    }


# ── Ranking ───────────────────────────────────────────────────

@app.post("/rank", response_model=RankResponse)
async def rank(req: RankRequest):
    if not _candidates:
        raise HTTPException(status_code=503, detail="Candidate pool not loaded")
    start = time.perf_counter()
    ranked = rank_candidates(_candidates, req.job, req.top_k)
    elapsed_ms = round((time.perf_counter() - start) * 1000, 1)
    return RankResponse(
        job_title=req.job.title,
        total_candidates_evaluated=len(_candidates),
        ranked_candidates=ranked,
        processing_time_ms=elapsed_ms,
    )
