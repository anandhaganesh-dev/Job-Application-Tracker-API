from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.base import Base
from app.db.session import engine
from app.models import user, job
from app.api.v1.router import router as v1_router

app = FastAPI(title="Job-Applications-Tracker-API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(v1_router)


@app.get("/")
def root():
    return {"message": "Job Application Tracker API is running"}
