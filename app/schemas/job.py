from pydantic import BaseModel
from datetime import date
from app.models.job import JobStatus


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
