import chromadb
from llama_index.core import Settings as LlamaSettings, VectorStoreIndex
from llama_index.vector_stores.chroma import ChromaVectorStore

from app.config import settings
from app.services.embedding_service import get_embed_model
from app.services.llm_factory import get_llm
from app.services.rag.base_rag import BaseRAGService


class BasicRAGService(BaseRAGService):
    def __init__(self):
        LlamaSettings._embed_model = get_embed_model()
        LlamaSettings._llm = get_llm()

        client = chromadb.PersistentClient(path=settings.VECTOR_STORE_PATH)
        collection = client.get_or_create_collection(settings.CHROMA_COLLECTION)
        vector_store = ChromaVectorStore(chroma_collection=collection)
        index = VectorStoreIndex.from_vector_store(vector_store)
        self.query_engine = index.as_query_engine(similarity_top_k=5)

    def query(self, question: str) -> dict:
        response = self.query_engine.query(question)
        sources = [
            {"file_path": node.metadata.get("file_path", "unknown"), "text": node.text[:200]}
            for node in response.source_nodes
        ]
        return {"response": str(response.response), "sources": sources}
