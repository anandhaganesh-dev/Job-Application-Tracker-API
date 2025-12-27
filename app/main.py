from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.models import user

app = FastAPI(title="Job-Applications-Tracker-API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Job Application Tracker API is running"}