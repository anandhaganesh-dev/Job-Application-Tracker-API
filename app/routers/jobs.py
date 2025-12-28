from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.schemas.job import JobResponse, JobCreate
from app.db.deps import get_db
from app.core.security import get_current_user
from app.services.job_services import create_job, get_user_jobs


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
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return get_user_jobs(db, current_user)
