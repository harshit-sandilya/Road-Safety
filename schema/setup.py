from pydantic import BaseModel


class CreateHandlerRequest(BaseModel):
    language: str
