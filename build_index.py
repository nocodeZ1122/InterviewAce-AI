from dotenv import load_dotenv 

load_dotenv()
from app.rag.loader import DocumentLoader
from app.rag.chunker import TextChunker
from app.rag.embedder import GeminiEmbedder
from app.rag.vector_store import VectorStore
from app.rag.retriever import Retriever
from app.rag.rag_service import RAGService

loader = DocumentLoader()
documents = loader.load_documents()

print(f"Loaded {len(documents)} documents")

chunker = TextChunker()

chunks = chunker.split(documents)

embedder = GeminiEmbedder()


print("\nGenerating embeddings...")

embeddings = []

for chunk in chunks:

    embedding = embedder.embed(
        chunk["content"]
    )

    embeddings.append(embedding)

print(f"Generated {len(embeddings)} embeddings")

store = VectorStore()

store.build(
    embeddings,
    chunks
)

store.save()





print("\nFAISS Index Saved Successfully!")
