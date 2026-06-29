from pydantic import BaseModel, Field
from typing import List, Optional

class WorkExperience(BaseModel):
    company: Optional[str] = ""
    title: Optional[str] = ""
    duration_months: Optional[int] = 0
    description: Optional[str] = ""

class Education(BaseModel):
    degree: Optional[str] = ""
    field: Optional[str] = ""
    institution: Optional[str] = ""

class ActivitySignals(BaseModel):
    github_active: Optional[bool] = False
    open_source_contributions: Optional[int] = 0
    blog_posts: Optional[int] = 0
    last_active_days_ago: Optional[int] = 180
    certifications_recent: Optional[int] = 0

class CandidateProfile(BaseModel):
    candidate_id: str
    name: str
    headline: Optional[str] = ""
    summary: Optional[str] = ""
    skills: List[str] = []
    total_experience_years: float = 0.0
    work_history: List[WorkExperience] = []
    education: List[Education] = []
    activity: Optional[ActivitySignals] = None
    location: Optional[str] = ""
    expected_role_level: Optional[str] = "mid"
    source: Optional[str] = "seed"  # "seed" or "uploaded"

class JobDescription(BaseModel):
    title: str
    description: str
    required_skills: Optional[List[str]] = []
    preferred_skills: Optional[List[str]] = []
    min_experience_years: Optional[float] = 0.0
    max_experience_years: Optional[float] = 20.0
    seniority_level: Optional[str] = "mid"
    domain: Optional[str] = ""

class RankRequest(BaseModel):
    job: JobDescription
    top_k: int = Field(default=10, ge=1, le=50)

class SignalBreakdown(BaseModel):
    semantic_similarity: float
    skills_match: float
    experience_fit: float
    activity_score: float
    seniority_fit: float

class RankedCandidate(BaseModel):
    rank: int
    candidate_id: str
    name: str
    headline: str
    skills: List[str]
    total_experience_years: float
    location: str
    final_score: float
    signals: SignalBreakdown
    ai_reasoning: str
    match_grade: str
    source: Optional[str] = "seed"

class RankResponse(BaseModel):
    job_title: str
    total_candidates_evaluated: int
    ranked_candidates: List[RankedCandidate]
    processing_time_ms: float
