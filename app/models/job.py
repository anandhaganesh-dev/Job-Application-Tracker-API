from enum import Enum as pyEnum
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Date
from datetime import date
from sqlalchemy.orm import relationship
from app.db.base import Base


class JobStatus(str, pyEnum):
    APPILIED = "APPLIED"
    INTERVIEW = "INTERVIEW"
    OFFER = "OFFER"
    REJECTED = "REJECTED"


class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, nullable=False)
    role = Column(String, nullable=False)
    status = Column(Enum(JobStatus), default=JobStatus.APPILIED)
    applied_date = Column(Date, default=date.today)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", backref="job_applications")
