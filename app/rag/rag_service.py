from app.rag.retriever import Retriever


class RAGService:

    def __init__(self):
        self.retriever = Retriever()

    def get_context(
        self,
        question,
        user_message: str,
        top_k: int = 3
    ):

        query = f"""
Question:
{question.title}

Description:
{question.description}

Difficulty:
{question.difficulty}

Topic:
{question.topic}

User Question:
{user_message}
"""

        results = self.retriever.retrieve(query, top_k)

        context = ""
        sources = []

        for chunk in results:

             context += chunk["content"]
             context += "\n\n"

             sources.append({
                 "topic": chunk["topic"],
                 "section": chunk["section"]
    })

        return {
                "context": context,
                 "sources": sources
        }  