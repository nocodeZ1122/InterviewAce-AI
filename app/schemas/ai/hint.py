from pydantic import BaseModel

class HintResponse(BaseModel):
    hint: str
    next_step: str