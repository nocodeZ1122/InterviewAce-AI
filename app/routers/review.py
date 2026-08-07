from fastapi import APIRouter

from app.schemas.review import (
    ReviewRequest,
    ReviewResponse
)

from app.services.review_service import ReviewService

router = APIRouter(
    prefix="/review",
    tags=["Review"]
)

review_service = ReviewService()


@router.post("", response_model=ReviewResponse)
async def review(request: ReviewRequest):

    result = review_service.review(
        question_id=request.question_id,
        code=request.code,
        language=request.language
    )

    return ReviewResponse(
        review=result
    )