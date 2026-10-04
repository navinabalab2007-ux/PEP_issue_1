from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from typing import Optional

from backend.database.database import get_db, ResumeAnalysis


router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "healthy"}


@router.post("/analyze-resume")
async def analyze_resume(
    resume: Optional[UploadFile] = File(None),
    job_description: str = Form(""),
    db: Session = Depends(get_db)
):
    # Dummy result for now.
    # The ML model will be connected here later.
    prediction = "Potential Fit"
    fit_score = 78

    # Save the analysis result to PostgreSQL.
    analysis = ResumeAnalysis(
        resume_filename=resume.filename if resume else None,
        job_description=job_description,
        prediction=prediction,
        fit_score=fit_score
    )

    db.add(analysis)
    db.commit()
    db.refresh(analysis)

    return {
        "prediction": prediction,
        "fit_score": fit_score
    }