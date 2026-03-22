import pytest

from app.services.embedding_service import get_embed_model


@pytest.mark.smoke
def test_embed_model_smoke_returns_embedding():
    model = get_embed_model()
    result = model.get_text_embedding("def hello(): pass")
    assert isinstance(result, list)
    assert len(result) > 0
