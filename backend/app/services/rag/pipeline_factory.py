from functools import lru_cache

from app.services.rag.base_rag import BaseRAGService


@lru_cache(maxsize=None)
def get_pipeline(name: str) -> BaseRAGService:
    if name == "basic":
        from app.services.rag.basic_rag import BasicRAGService

        return BasicRAGService()
    raise ValueError(f"Unknown pipeline: {name}")
