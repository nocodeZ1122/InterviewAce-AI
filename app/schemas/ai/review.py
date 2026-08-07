from pydantic import BaseModel

class ReviewResponse(BaseModel):
    correctness: str
    bugs: list[str]
    time_complexity: str
    space_complexity: str
    edge_cases: list[str]
    interview_feedback: str
    optimized_solution: str
    
