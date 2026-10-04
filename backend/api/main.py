from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.routes import router
from backend.database.database import Base, engine
from backend.database.database import ResumeAnalysis


app = FastAPI(
    title="Resume Analysis & Ranking API",
    description="Backend API for resume analysis and ranking.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(router)


@app.get("/")
def root():
    return {"message": "Resume Analysis API is running"}