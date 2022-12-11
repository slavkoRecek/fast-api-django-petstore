from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.get("/", response_model=list[Any])
def list_pets(offset: int = 0, limit: int = 10) -> Any:
    """
    Endpoint to get multiple posts based on offset and limit values.
    """
    return [{
        "message": "Hello World",
    }]
