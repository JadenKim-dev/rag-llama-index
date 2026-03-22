from llama_index.core import Document
from llama_index.core.schema import TextNode

from app.chunkers.code_splitter import get_code_nodes
from app.chunkers.metadata_enricher import enrich_nodes

SAMPLE_PYTHON = """\
class UserService:
    def get_user(self, user_id: int):
        return {"id": user_id}

    def create_user(self, name: str):
        return {"name": name}
"""


def test_code_splitter_returns_nodes():
    doc = Document(text=SAMPLE_PYTHON, metadata={"file_path": "services/user.py", "language": "python"})
    nodes = get_code_nodes([doc], language="python")
    assert nodes


def test_metadata_enricher_fills_missing_fields():
    bare_node = TextNode(text="def foo(): pass")
    enriched = enrich_nodes([bare_node])
    assert enriched[0].metadata["file_path"] == "unknown"
    assert enriched[0].metadata["language"] == "python"


def test_metadata_enricher_sets_excluded_llm_keys():
    node = TextNode(text="def foo(): pass")
    enriched = enrich_nodes([node])
    assert "file_path" in enriched[0].excluded_llm_metadata_keys
    assert "language" in enriched[0].excluded_llm_metadata_keys
