import os
#from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
#load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

DATABASE_URL = "postgresql://postgres:rishi@localhost:5432/interviewace_ai"
engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
