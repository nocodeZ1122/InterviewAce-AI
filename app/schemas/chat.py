from pydantic import BaseModel
from typing import Literal


class ChatRequest(BaseModel):
    question_id: int
    message: str
    mode: Literal[
        "explain",
        "hint",
        "dry_run",
        "review"
    ] = "explain"


class ChatResponse(BaseModel):
    reply: str