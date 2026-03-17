from llama_index.core.schema import BaseNode


def enrich_nodes(nodes: list[BaseNode]) -> list[BaseNode]:
    for node in nodes:
        node.metadata.setdefault("file_path", "unknown")
        node.metadata.setdefault("language", "python")
        node.excluded_llm_metadata_keys = ["file_path", "language"]
        node.excluded_embed_metadata_keys = []
    return nodes
