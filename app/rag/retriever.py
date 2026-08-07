import numpy as np

from app.rag.embedder import GeminiEmbedder
from app.rag.vector_store import VectorStore


class Retriever:

    def __init__(self):

        self.embedder = GeminiEmbedder()

        self.store = VectorStore()

        self.store.load()


    def retrieve(
        self,
        query: str,
        top_k: int = 3
    ):

        query_embedding = self.embedder.embed(query)

        query_vector = np.array(
            [query_embedding],
            dtype="float32"
        )

        distances, indices = self.store.index.search(
            query_vector,
            top_k
        )

        results = []

        for idx in indices[0]:

            if idx == -1:
                continue

            results.append(
                self.store.documents[idx]
    )

        return results