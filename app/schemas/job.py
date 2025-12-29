from pydantic import BaseModel, Field
from datetime import date
from app.models.job import JobStatus
from typing import Optional


class JobCreate(BaseModel):
    company: str = Field(..., min_length=2)
    role: str = Field(..., min_length=2)
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
    company: Optional[str] = Field(default=None, min_length=2)
    role: Optional[str] = Field(default=None, min_length=2)
    status: Optional[JobStatus] = None
    applied_date: Optional[date] = None

    class Config:
        from_attributes = True
