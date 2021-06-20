from fastapi import APIRouter
from routes import patients

router = APIRouter()
router.include_router(patients.router, tags=["patients"], prefix="/patients")

