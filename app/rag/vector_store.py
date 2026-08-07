import faiss
import numpy as np


class VectorStore:

    def __init__(self):

        self.index = None

        self.documents = []

    def build(self, embeddings, chunks):

        dimension = len(embeddings[0])

        self.index = faiss.IndexFlatL2(dimension)

        vectors = np.array(embeddings).astype("float32")

        self.index.add(vectors)

        self.documents = chunks

    def save(self):

        faiss.write_index(self.index, "knowledge.index")

        np.save(
            "knowledge_chunks.npy",
            self.documents,
            allow_pickle=True
        )

    def load(self):

        self.index = faiss.read_index("knowledge.index")

        self.documents = np.load(
            "knowledge_chunks.npy",
            allow_pickle=True
        ).tolist()