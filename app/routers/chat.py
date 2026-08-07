from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter(prefix="/chat", tags=["Chat"])

chat_service = ChatService()


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):

    reply = chat_service.chat(
    session_id="default",
    question_id=request.question_id,
    message=request.message,
    mode=request.mode
)

    return ChatResponse(reply=reply)