from application.pets.models import Pet
from application.pets.payloads import PetOut, PetIn


class PetService:
    async def list_pets(self):
        list = []
        async for entry in Pet.objects.all():
            list.append(PetOut.from_model(entry))
        return list

    def create_pet(self, pet: PetIn):
        pet = Pet.objects.create(name=pet.name, status=pet.status)
        return PetOut.from_model(pet)


pet_service: PetService = PetService()
