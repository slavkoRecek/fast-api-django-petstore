from pydantic import BaseModel, EmailStr

from application.users.models import User


class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    phone: str


class UserOut(UserBase):
    id: int

    @classmethod
    def from_model(cls, db_user: User):
        return cls(
            id=db_user.id,
            email=db_user.email,
            first_name=db_user.first_name,
            last_name=db_user.last_name,
            phone=db_user.phone,
        )


class UserIn(UserBase):
    password: str
    repeated_password: str
