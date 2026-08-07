from pydantic import BaseModel
from enum import Enum


class Difficulty(str, Enum):
    easy = "Easy"
    medium = "Medium"
    hard = "Hard"


class QuestionBase(BaseModel):
    title: str
    description: str
    difficulty: Difficulty
    topic: str
    companies: str
    examples: str
    constraints: str
    leetcode_id: int | None = None
    leetcode_url: str | None = None


class QuestionCreate(QuestionBase):
    pass


class QuestionUpdate(QuestionBase):
    pass


class QuestionResponse(QuestionBase):
    id: int

    class Config:
        from_attributes = True