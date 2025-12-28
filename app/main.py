from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.models import user
from app.routers import auth, users

app = FastAPI(title="Job-Applications-Tracker-API")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(users.router)


@app.get("/")
def root():
    return {"message": "Job Application Tracker API is running"}
