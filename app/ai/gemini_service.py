import os
import json

from dotenv import load_dotenv
from google import genai
from app.ai.prompt_builder import (
    build_explanation_prompt,
    build_hint_prompt,
    build_review_prompt,
    build_dry_run_prompt,
)
from app.ai.context_builder import build_question_context
from app.services.question_service import get_question_by_id
from app.database.connection import SessionLocal

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def ask_gemini(
    question,
    prompt: str,
    mode: str = "explain",
    history: str = "",
    rag_context: str = ""
):
    db = SessionLocal()

    question_data = get_question_by_id(db, question)

    question_context = build_question_context(question_data)  # scheme prompting

    db.close()
    
    if mode == "hint":
        system_prompt = build_hint_prompt(prompt)

    elif mode == "dry_run":
        system_prompt = build_dry_run_prompt(prompt)

    elif mode == "review":
        system_prompt = build_review_prompt(...)

    else:
        system_prompt = build_explanation_prompt(prompt)

   

    final_prompt = f"""
# ROLE

You are InterviewAce AI, an expert coding interview mentor.

Your goal is NOT to simply give answers.

Your goal is to help the user think like a software engineer.

Guide the user progressively.

If hints are requested, never reveal the full solution immediately.

If explanations are requested, explain the intuition before the implementation.

Use the retrieved interview notes whenever they are relevant.

If they are not relevant, ignore them completely.

Never hallucinate information.

---

# LEETCODE QUESTION

{question_context}

---

# RETRIEVED KNOWLEDGE

{rag_context}

---

# CONVERSATION HISTORY

{history}

---

# USER MESSAGE

{prompt}

---

# RESPONSE FORMAT

Always answer using beautiful Markdown.

Follow these rules:

- Use clear headings (##).
- Leave one blank line between paragraphs.
- Use bullet points wherever appropriate.
- Use numbered lists for step-by-step explanations.
- Wrap all code inside triple backticks with the correct language.
- Use tables whenever comparing approaches or complexities.
- Never produce one large wall of text.
- Keep paragraphs between 2–4 lines.
- Highlight important terms using **bold**.
- Use inline code formatting (`code`) for variables, functions, and complexity notation.
- End with a short "Key Takeaway" section whenever appropriate.
- Return only valid Markdown.
- Never use JSON.
- Never use LaTeX.
- Never use mathematical notation such as:
      - \frac{{}}
      - $
      - \[
      - \]
- Write complexities in plain text:
    - O(1)
    - O(log n)
    - O(n)
    - O(n log n)

- Use **bold headings** instead of bullet points for sections like Time Complexity and Space Complexity.

Example:

**Time Complexity:** O(n)

Explain why.

**Space Complexity:** O(n)

Explain why.
---

# MODE SPECIFIC INSTRUCTIONS

{system_prompt}
"""
    
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=final_prompt,
        )
        import json

        
        return response.text

    except Exception as e:
        
        return f"Gemini Error :{e}"
