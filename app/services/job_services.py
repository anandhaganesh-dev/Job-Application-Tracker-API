from sqlalchemy.orm import Session
from datetime import date
from app.models.job import JobApplication
from app.schemas.job import JobCreate
from app.models.user import User


def create_job(db: Session, job: JobCreate, user: User):
    db_job = JobApplication(
        company=job.company,
        role=job.role,
        status=job.status,
        applied_date=job.applied_date or date.today(),
        user_id=user.id,
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job


def get_user_jobs(db: Session, user: User):
    return db.query(JobApplication).filter(JobApplication.user_id == user.id).all()
