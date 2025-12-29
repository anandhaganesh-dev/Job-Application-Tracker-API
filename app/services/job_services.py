from sqlalchemy.orm import Session
from datetime import date
from app.models.job import JobApplication
from app.schemas.job import JobCreate, JobUpdate, JobStatus
from app.models.user import User
from fastapi import HTTPException, status


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


def get_user_jobs(
    db: Session,
    user: User,
    status: JobStatus | None = None,
    limit: int = 10,
    offset: int = 0,
):
    query = db.query(JobApplication).filter(JobApplication.user_id == user.id)
    if status:
        query = query.filter(JobApplication.status == status)
    return query.offset(offset).limit(limit).all()


def get_job_by_id(db: Session, job_id: int, user: User):
    job = (
        db.query(JobApplication)
        .filter(JobApplication.id == job_id, JobApplication.user_id == user.id)
        .first()
    )
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Job application not found"
        )
    return job


def update_job(db: Session, job: JobApplication, job_update: JobUpdate):
    for field, value in job_update.dict(exclude_unset=True).items():
        setattr(job, field, value)

    db.commit()
    db.refresh(job)
    return job


def delete_job(db: Session, job: JobApplication):
    db.delete(job)
    db.commit()
