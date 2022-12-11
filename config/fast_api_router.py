from pets.endpoints import router as pet_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(pet_router, prefix="/pets", tags=["Pets"])
