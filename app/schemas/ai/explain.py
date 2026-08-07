from pydantic import BaseModel

class ExplainResponse(BaseModel):
    concept: str
    intuition: str
    algorithm: str
    time_complexity: str
    space_complexity: str
    python_code: str
    common_mistakes: list[str]