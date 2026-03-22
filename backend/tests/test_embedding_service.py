from unittest.mock import patch

from app.services.embedding_service import get_embed_model


def test_embed_model_returns_embedding():
    get_embed_model.cache_clear()
    with patch("app.services.embedding_service.HuggingFaceEmbedding") as mock_cls:
        instance = mock_cls.return_value
        model = get_embed_model()
        assert model is instance
        mock_cls.assert_called_once()


def test_embed_model_singleton():
    get_embed_model.cache_clear()
    with patch("app.services.embedding_service.HuggingFaceEmbedding") as mock_cls:
        model1 = get_embed_model()
        model2 = get_embed_model()
        assert model1 is model2
        mock_cls.assert_called_once()
