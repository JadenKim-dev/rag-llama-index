from unittest.mock import MagicMock, patch

from app.services.rag.basic_rag import BasicRAGService


def test_basic_rag_query_returns_response():
    with patch("app.services.rag.basic_rag.get_embed_model"), patch(
        "app.services.rag.basic_rag.get_llm"
    ), patch("app.services.rag.basic_rag.chromadb"), patch(
        "app.services.rag.basic_rag.VectorStoreIndex"
    ) as mock_index_cls, patch("app.services.rag.basic_rag.ChromaVectorStore"):
        mock_engine = MagicMock()
        mock_engine.query.return_value = MagicMock(response="test response", source_nodes=[])
        mock_index_cls.from_vector_store.return_value.as_query_engine.return_value = mock_engine
        svc = BasicRAGService()
        result = svc.query("테스트 질문")
        assert result["response"] == "test response"


def test_pipeline_factory_returns_basic():
    from app.services.rag.pipeline_factory import get_pipeline

    with patch("app.services.rag.basic_rag.get_embed_model"), patch(
        "app.services.rag.basic_rag.get_llm"
    ), patch("app.services.rag.basic_rag.chromadb"), patch(
        "app.services.rag.basic_rag.VectorStoreIndex"
    ), patch("app.services.rag.basic_rag.ChromaVectorStore"):
        get_pipeline.cache_clear()
        pipeline = get_pipeline("basic")
        assert pipeline.__class__.__name__ == "BasicRAGService"
