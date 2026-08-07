from fastapi import APIRouter
from app.ai.gemini_service import ask_gemini
from app.schemas.ai.explain import ExplainResponse
from app.schemas.ai.hint import HintResponse

router = APIRouter(prefix="/ai", tags=["AI"])



@router.get("/explain")
async def explain(question: int, prompt: str):
    return ask_gemini(question, prompt)


@router.get("/hint")
async def hint(question: int, prompt: str):
    return ask_gemini(question, prompt, mode="hint")

#@router.post("/review") 
#async def review(question:int, prompt:str):


