from fastapi import APIRouter

from application.pets.payloads import PetOut, PetIn
from application.pets.service import pet_service
from application.shared.error_handling import error_response_dict

router = APIRouter()


@router.get("/", response_model=list[PetOut])
async def list_pets(offset: int = 0, limit: int = 10) -> list[PetOut]:
    response_list = await pet_service.list_pets()
    return response_list

# post operation to crate a new pet
@router.post("/", response_model=PetOut, status_code=201, responses=error_response_dict)
def create_pet(pet: PetIn) -> PetOut:
    created_pet = pet_service.create_pet(pet)
    # return 201 status code with the created pet
    return created_pet
