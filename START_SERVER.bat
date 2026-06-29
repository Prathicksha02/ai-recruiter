@echo off
echo ============================================
echo   AI Recruiter - Starting Backend Server
echo ============================================

cd /d "%~dp0backend"

echo.
echo [1/3] Checking Python...
python --version
if errorlevel 1 (echo ERROR: Python not found. Install from python.org & pause & exit)

echo.
echo [2/3] Installing dependencies (first time only)...
pip install -r requirements.txt

echo.
echo [3/3] Starting FastAPI server on http://localhost:8001
echo.
echo  Open frontend\index.html in your browser after server starts!
echo  Press Ctrl+C to stop.
echo.
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8001
pause
