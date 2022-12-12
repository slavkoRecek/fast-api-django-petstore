from fastapi import APIRouter

from config.pets.payloads import PetOut
from config.pets.service import pet_service

router = APIRouter()


@router.get("/", response_model=list[PetOut])
def list_pets(offset: int = 0, limit: int = 10) -> list[PetOut]:
    response_list = pet_service.list_pets()
    return response_list
