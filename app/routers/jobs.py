from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.schemas.job import JobResponse, JobCreate, JobUpdate
from app.db.deps import get_db
from app.core.security import get_current_user
from app.services.job_services import (
    create_job,
    get_user_jobs,
    get_job_by_id,
    update_job,
    delete_job,
)
from app.models.job import JobStatus


router = APIRouter(prefix="/jobs", tags=["Jobs"])


@router.post("/", response_model=JobResponse, status_code=status.HTTP_201_CREATED)
def create_job_applications(
    job: JobCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return create_job(db, job, current_user)


@router.get("/", response_model=list[JobResponse])
def list_my_jobs(
    status: JobStatus | None = None,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return get_user_jobs(db, current_user, status)


@router.put("/{job_id}", response_model=JobResponse)
def update_job_applications(
    job_id: int,
    job_update: JobUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    job = get_job_by_id(db, job_id, current_user)
    return update_job(db, job, job_update)


@router.delete("/{job_id}", status_code=status.HTTP_404_NOT_FOUND)
def delete_job_applications(
    job_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)
):
    job = get_job_by_id(db, job_id, current_user)
    return delete_job(db, job)
