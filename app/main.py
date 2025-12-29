from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.base import Base
from app.db.session import engine
from app.models import user, job
from app.routers import auth, users, jobs

app = FastAPI(title="Job-Applications-Tracker-API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(jobs.router)


@app.get("/")
def root():
    return {"message": "Job Application Tracker API is running"}
