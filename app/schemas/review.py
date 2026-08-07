from pydantic import BaseModel


class ReviewRequest(BaseModel):

    question_id: int

    language: str

    code: str


class ReviewResponse(BaseModel):

    review: str