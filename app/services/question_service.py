from sqlalchemy.orm import Session  # talks to postgres
from app.models.question import Question  # question table
from sqlalchemy.orm import Session
from app.models.question import Question
from fastapi import HTTPException


def get_all_questions(db: Session):
    return db.query(Question).all()


def search_questions(db: Session, topic: str):
    return db.query(Question).filter(Question.topic == topic).all()


def search_by_difficulty(db: Session, difficulty: str):
    return db.query(Question).filter(Question.difficulty == difficulty).all()


def get_questions_paginated(db: Session, skip: int, limit: int):
    return db.query(Question).offset(skip).limit(limit).all()


def create_question(db: Session, question_data):
    db_question = Question(
        title=question_data.title,
        description=question_data.description,
        difficulty=question_data.difficulty.value,
        topic=question_data.topic.value,
        companies=str(question_data.companies),
        examples=str(question_data.examples),
        constraints=str(question_data.constraints),
    )

    db.add(db_question)
    db.commit()
    db.refresh(db_question)

    return db_question


def get_question_by_id(db: Session, id: int):
    question = db.query(Question).filter(Question.id == id).first()

    if not question:
        raise HTTPException(
            status_code=404,
            detail="Question Not Found"
        )

    return question
def update_question(db: Session, id: int, question_data):
    db_question = db.query(Question).filter(Question.id == id).first()

    if not db_question:
        raise HTTPException(
            status_code=404,
            detail="Question Not Found"
        )

    db_question.title = question_data.title
    db_question.description = question_data.description
    db_question.difficulty = question_data.difficulty.value
    db_question.topic = question_data.topic.value
    db_question.companies = str(question_data.companies)
    db_question.examples = str(question_data.examples)
    db_question.constraints = str(question_data.constraints)

    db.commit()
    db.refresh(db_question)

    return db_question
def delete_question(db: Session, id: int):
    db_question = db.query(Question).filter(Question.id == id).first()

    if not db_question:
        raise HTTPException(
            status_code=404,
            detail="Question Not Found"
        )

    db.delete(db_question)
    db.commit()

    return {
        "message": "Question Deleted Successfully"
    }