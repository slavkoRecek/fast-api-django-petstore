from pydantic import BaseModel


class PetOut(BaseModel):
    id: int
    name: str
    status: str

    @classmethod
    def from_model(cls, db_pet):
        return cls(
            id=db_pet.id,
            name=db_pet.name,
            status=db_pet.status,
        )
