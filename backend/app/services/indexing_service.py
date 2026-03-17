import os
import pickle
from pathlib import Path

import chromadb
from llama_index.core import Document, Settings as LlamaSettings, VectorStoreIndex
from llama_index.vector_stores.chroma import ChromaVectorStore

from app.chunkers.code_splitter import get_code_nodes
from app.chunkers.metadata_enricher import enrich_nodes
from app.config import settings
from app.services.embedding_service import get_embed_model

SUPPORTED_EXTENSIONS = {".py": "python", ".js": "javascript", ".ts": "typescript", ".go": "go"}


def index_codebase(directory: str) -> int:
    LlamaSettings._embed_model = get_embed_model()

    documents = []
    for path in Path(directory).rglob("*"):
        if path.suffix in SUPPORTED_EXTENSIONS:
            text = path.read_text(encoding="utf-8", errors="ignore")
            documents.append(
                Document(
                    text=text,
                    metadata={"file_path": str(path), "language": SUPPORTED_EXTENSIONS[path.suffix]},
                )
            )

    all_nodes = []
    for doc in documents:
        language = doc.metadata["language"]
        all_nodes.extend(enrich_nodes(get_code_nodes([doc], language=language)))

    os.makedirs(settings.VECTOR_STORE_PATH, exist_ok=True)
    client = chromadb.PersistentClient(path=settings.VECTOR_STORE_PATH)
    collection = client.get_or_create_collection(settings.CHROMA_COLLECTION)
    vector_store = ChromaVectorStore(chroma_collection=collection)
    VectorStoreIndex(nodes=all_nodes, vector_store=vector_store)

    nodes_path = os.path.join(settings.VECTOR_STORE_PATH, "nodes.pkl")
    with open(nodes_path, "wb") as file:
        pickle.dump(all_nodes, file)

    return len(all_nodes)
