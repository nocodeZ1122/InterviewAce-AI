from sqlalchemy import Column, Integer, String
from app.database.connection import Base


class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    difficulty = Column(String, nullable=False)
    topic = Column(String, nullable=False)
    companies = Column(String, nullable=False)
    examples = Column(String, nullable=False)
    constraints = Column(String, nullable=False)
    leetcode_id = Column(Integer)
    leetcode_url = Column(String)


