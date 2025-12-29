from pydantic import BaseModel
from datetime import date
from app.models.job import JobStatus
from typing import Optional


class JobCreate(BaseModel):
    company: str
    role: str
    status: JobStatus = JobStatus.APPILIED
    applied_date: date | None = None


class JobResponse(BaseModel):
    id: int
    company: str
    role: str
    status: JobStatus
    applied_date: date

    class Config:
        from_attributes = True


class JobUpdate(BaseModel):
    company: Optional[str] = None
    role: Optional[str] = None
    status: Optional[JobStatus] = None
    applied_date: Optional[date] = None
