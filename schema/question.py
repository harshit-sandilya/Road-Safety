from pydantic import BaseModel


class QuestionRequest(BaseModel):
    handler_id: int
    question: str
