from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from app.models.question import Question
from app.database.connection import Base, engine
from app.routers.questions import router
from app.routers.ai import router as ai_router
from app.routers.chat import router as chat_router
from app.routers.review import router as review_router


app = FastAPI(
    title="InterviewAce AI",
    description="AI-powered developer interview platform",
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)
app.include_router(router)
app.include_router(ai_router)
app.include_router(chat_router)
app.include_router(review_router)


@app.get("/")
async def home():
    return {"project": "InterviewAce AI", "version": "1.0.0", "status": "Running"}


@app.get("/health")
async def health():
    return {"status": "running"}


@app.get("/about")
async def info():
    return {"author": "rishi", "name": "xyz"}
