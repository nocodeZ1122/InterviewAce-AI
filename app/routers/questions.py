from fastapi import APIRouter
from app.schemas.question import (
    QuestionCreate,
    QuestionUpdate,
    QuestionResponse
)
from sqlalchemy.orm import Session
from fastapi import Depends
from app.models.question import Question as QuestionModel
from fastapi import HTTPException
from app.database.connection import get_db
from app.services import question_service

router = APIRouter(prefix="/questions", tags=["Questions"])
# so you dont have to write questions again it takes it automatically for calling in the url



@router.post("/", response_model=QuestionResponse)
async def create_question(
    question: QuestionCreate,
    db: Session = Depends(get_db)
):
    return question_service.create_question(db, question)



@router.get("/", response_model=list[QuestionResponse])
async def get_questions(db: Session = Depends(get_db)):
    return question_service.get_all_questions(db)


@router.get("/{id}", response_model=QuestionResponse)
async def get_question(id: int, db: Session = Depends(get_db)):
   return question_service.get_question_by_id(db, id) 



@router.put("/{id}", response_model=QuestionResponse)
async def update_question(
    id: int,
    question: QuestionUpdate,
    db: Session = Depends(get_db)
):
    return question_service.update_question(
        db,
        id,
        question
    )


@router.delete("/{id}")
async def delete_question(
    id: int,
    db: Session = Depends(get_db)
):
    return question_service.delete_question(db, id)

@router.get("/search")
async def search_questions(
    topic: str,
    db: Session = Depends(get_db)
):
    return question_service.search_questions(db, topic)

@router.get("/difficulty")
async def get_by_difficulty(
    difficulty: str,
    db: Session = Depends(get_db)
):
    return question_service.search_by_difficulty(db, difficulty)

@router.get("/paginated")
async def get_questions_paginated(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db) 
):
    return question_service.get_questions_paginated(db, skip, limit) 
