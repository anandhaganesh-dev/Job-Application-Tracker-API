from fastapi import APIRouter
from app.api.v1 import auth, jobs, users

router = APIRouter(prefix="/api/v1")

router.include_router(auth.router, tags=["Auth"])
router.include_router(users.router, tags=["Users"])
router.include_router(jobs.router, tags=["Jobs"])
