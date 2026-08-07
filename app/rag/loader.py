from pathlib import Path


class DocumentLoader:

    def __init__(self, knowledge_dir: str = "knowledge"):
        self.knowledge_dir = Path(knowledge_dir)

    def load_documents(self):

        documents = []

        for file in self.knowledge_dir.rglob("*.md"):

            with open(file, "r", encoding="utf-8") as f:

                text = f.read()

                documents.append({

                    "path": str(file),

                    "content": text

                })

        return documents