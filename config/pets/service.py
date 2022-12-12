from config.pets.models import Pet
from config.pets.payloads import PetOut


class PetService:
    def list_pets(self):
        db_pets = Pet.objects.all()
        return [PetOut.from_model(db_pet) for db_pet in db_pets]


pet_service: PetService = PetService()
