from functools import lru_cache

from llama_index.embeddings.huggingface import HuggingFaceEmbedding

from app.config import settings


@lru_cache(maxsize=1)
def get_embed_model() -> HuggingFaceEmbedding:
    return HuggingFaceEmbedding(
        model_name="jinaai/jina-embeddings-v2-base-code",
        trust_remote_code=True,
        device=settings.EMBED_DEVICE,
    )
