from pydantic import BaseModel


class ErrorResponse(BaseModel):
    error: str


class SuccessResponse(BaseModel):
    status: str = "ok"
    message: str = ""
