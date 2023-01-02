import logging

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse

logger = logging.getLogger(__name__)


class Error(BaseModel):
    message: str
    code: str | None = None
    detail: dict | None = None

    @classmethod
    def from_validation_errors(cls, raw_errors):
        errors = []
        for raw_error in raw_errors:
            exc = raw_error.exc
            if isinstance(exc, ValidationError):
                for field_error in exc.errors():
                    error = cls(
                        code='validation_error',
                        message=f"Field '{field_error['loc'][0]}' is invalid. {field_error['msg']}",
                        detail={
                            'model_class': exc.model.__name__,
                            'field': field_error['loc'][0],
                        }
                    )
                    errors.append(error)
            else:
                logger.error(f"Unhandled error: {exc}")
        return errors


class ErrorResponse(BaseModel):
    status_code: int
    errors: list[Error]


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(ValueError)
    async def value_error_exception_handler(request: Request, exc: ValueError) -> JSONResponse:
        body = ErrorResponse(
            status_code=422,
            errors=[{"message": exc.args[0]}])
        return JSONResponse(
            status_code=422,
            content=body.dict(),
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request, exc: RequestValidationError) -> JSONResponse:
        body = ErrorResponse(
            status_code=422,
            errors=Error.from_validation_errors(exc.raw_errors))
        return JSONResponse(
            status_code=422,
            content=body.dict(),
        )


error_response_dict = {422: {"model": ErrorResponse}}
