from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from application.shared.error_handling import error_response_dict
from application.users.payloads import UserIn, UserOut, Token
from application.users.service import user_service, authentication_service

router = APIRouter()


@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED, responses=error_response_dict)
def register_user(user: UserIn) -> UserOut:
    user = user_service.register_user(user)
    # return 201 status code with the created pet
    return user


@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authentication_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    # TODO: generate token
    return access_token

