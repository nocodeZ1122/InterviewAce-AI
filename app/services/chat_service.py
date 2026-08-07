from app.ai.gemini_service import ask_gemini
from app.memory import memory
from app.database.connection import SessionLocal
from app.services.question_service import get_question_by_id
from app.rag.rag_service import RAGService


class ChatService:
    def __init__(self):
        self.rag = RAGService()

    def chat(self, session_id: str, question_id: int, message: str, mode: str):

        session_id = str(question_id)


        history = memory.get_history(session_id)

        db = SessionLocal()

        question = get_question_by_id(db, question_id)

        db.close()

        rag = self.rag.get_context(question, message)

        context = rag["context"]
        sources = rag["sources"]
        reply = ask_gemini(
             question=question_id,
            prompt=message,
            mode=mode,
            history=history,
            rag_context=context,
        )

        memory.add_user_message(session_id, message)
        memory.add_ai_message(session_id, reply)

        return reply
