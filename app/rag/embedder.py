import os

from google import genai


class GeminiEmbedder:

    def __init__(self):

        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        self.model = "gemini-embedding-001"


    def embed(self, text: str):

        response = self.client.models.embed_content(

            model=self.model,

            contents=text

        )

        return response.embeddings[0].values