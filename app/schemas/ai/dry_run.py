from pydantic import BaseModel #Every AI feature gets its own schema

class DryRunStep(BaseModel):
    iteration: int
    variables: dict[str, str]
    decision: str
    explanation: str

class DryRunResponse(BaseModel):
    steps: list[DryRunStep]
    result: str