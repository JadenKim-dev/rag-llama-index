from unittest.mock import MagicMock, patch

import pytest

from app.config import Settings
from app.services.llm_factory import get_llm


def test_get_llm_ollama():
    mock_ollama_cls = MagicMock()
    with patch("app.services.llm_factory.settings", Settings(LLM_PROVIDER="ollama")), patch(
        "llama_index.llms.ollama.Ollama", mock_ollama_cls
    ):
        get_llm()
        mock_ollama_cls.assert_called_once()


def test_get_llm_unknown_provider_raises():
    with patch("app.services.llm_factory.settings", Settings(LLM_PROVIDER="unknown")):
        with pytest.raises(ValueError, match="Unknown LLM provider"):
            get_llm()
