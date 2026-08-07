import json
import os

from app.database.connection import SessionLocal
from app.models.question import Question

DATA_FOLDER = "data/company_questions/company-wise-leetcode-main"


def import_questions():
    db = SessionLocal()

    for filename in os.listdir(DATA_FOLDER):
        if not filename.endswith(".json"):
            continue

        company = filename.replace(".json", "")

        file_path = os.path.join(DATA_FOLDER, filename)

        with open(file_path, "r", encoding="utf-8") as f:
            questions = json.load(f)

        print(f"Importing {company}...")
        for question in questions:
            db_question = Question(
                leetcode_id=question["ID"],
                leetcode_url=question["Leetcode Question Link"].strip(),
                title=question["Title"],
                description="",
                difficulty=question["Difficulty"],
                topic="",
                companies=company,
                examples="",
                constraints="",
            )
            db.add(db_question)

        db.commit()

    db.close()
    print("Import Complete!")


if __name__ == "__main__":
    import_questions()
