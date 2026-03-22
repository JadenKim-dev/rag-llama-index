from llama_index.core import Document
from llama_index.core.node_parser import CodeSplitter
from llama_index.core.schema import BaseNode


def get_code_nodes(
    documents: list[Document],
    language: str = "python",
    chunk_lines: int = 40,
    chunk_lines_overlap: int = 15,
    max_chars: int = 1500,
) -> list[BaseNode]:
    splitter = CodeSplitter(
        language=language,
        chunk_lines=chunk_lines,
        chunk_lines_overlap=chunk_lines_overlap,
        max_chars=max_chars,
    )
    return splitter.get_nodes_from_documents(documents)
