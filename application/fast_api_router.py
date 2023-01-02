from application.pets.endpoints import router as pet_router
from application.users.endpoints import router as user_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(pet_router, prefix="/pets", tags=["Pets"])
router.include_router(user_router, prefix="/users", tags=["Users"])
