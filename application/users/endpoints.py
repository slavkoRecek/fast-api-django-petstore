from fastapi import APIRouter

from application.shared.error_handling import error_response_dict
from application.users.payloads import UserIn, UserOut
from application.users.service import user_service

router = APIRouter()


@router.post("/", response_model=UserOut, status_code=201, responses=error_response_dict)
def register_user(user: UserIn) -> UserOut:
    user = user_service.register_user(user)
    # return 201 status code with the created pet
    return user
