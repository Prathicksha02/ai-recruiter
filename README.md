# 🤖 AI Recruiter – Intelligent Resume Ranking System

An AI-powered recruitment system that intelligently ranks candidates based on semantic understanding of job descriptions, resume analysis, and multiple hiring signals.

##  Overview

Traditional Applicant Tracking Systems (ATS) rely heavily on keyword matching, often overlooking highly qualified candidates.

AI Recruiter addresses this limitation by using semantic matching, skill analysis, experience evaluation, and candidate profile signals to generate a highly accurate ranked shortlist for recruiters.

---

##  Features

-  Upload Job Description (PDF, DOCX, TXT)
-  Extract Job Description Automatically
-  Upload Candidate Resume
-  AI-Based Resume Parsing
-  Semantic Job-Candidate Matching
-  Required & Preferred Skill Matching
-  Candidate Ranking with Match Scores
-  Signal-Based Evaluation
  - Semantic Similarity
  - Skills Match
  - Experience Fit
  - Seniority Fit
  - Activity Score
-  Candidate Detail Popup
-  Fast Candidate Ranking

---

## 🖥️ Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- FastAPI

### AI / NLP
- Sentence Transformers
- Resume Parsing
- Semantic Similarity

---

## 📂 Project Structure

```
ai-recruiter/
│
├── backend/
│   ├── core/
│   ├── data/
│   ├── services/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   └── index.html
│
├── START_SERVER.bat
├── .gitignore
└── README.md
```

---

##  How to Run

### 1. Clone Repository

```bash
git clone https://github.com/Prathicksha02/ai-recruiter.git
```

### 2. Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn main:app --reload --port 8001
```

Backend runs at:

```
http://127.0.0.1:8001
```

### 3. Frontend

Open

```
frontend/index.html
```

using Live Server in VS Code.

---

##  Workflow

1. Upload a Job Description or paste the text.
2. Extract the Job Description.
3. Upload candidate resumes.
4. AI parses the resumes.
5. AI evaluates each candidate.
6. Candidates are ranked using multiple evaluation signals.
7. Recruiter can view detailed candidate information.

---

## 📊 Ranking Signals

The final score is computed using multiple factors:

- Semantic Similarity
- Required Skills Match
- Preferred Skills Match
- Experience Fit
- Seniority Match
- Candidate Activity Score

---

##  Key Highlights

- Context-aware semantic matching
- Intelligent candidate ranking
- Explainable AI reasoning
- Interactive recruiter dashboard
- Modern responsive UI

---


## 👩‍💻 Developed By

**Prathicksha M**

Department of Computer Science and Engineering

St. Joseph's Institute of Technology

---

##  License

This project was developed as a hackathon Proof of Concept for intelligent AI-powered recruitment.
