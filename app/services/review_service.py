from app.ai.gemini_service import client
from app.ai.review_prompt import build_review_prompt
from app.ai.context_builder import build_question_context
from app.services.question_service import get_question_by_id
from app.database.connection import SessionLocal


class ReviewService:

    def review(self, question_id: int, code: str, language: str):

        db = SessionLocal()

        question = get_question_by_id(db, question_id)

        context = build_question_context(question)

        db.close()

        prompt = build_review_prompt(
            context,
            code,
            language
        )

        try:

            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            return f"Gemini Error:\n{str(e)}"