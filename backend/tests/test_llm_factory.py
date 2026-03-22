from unittest.mock import MagicMock, patch

import pytest

from app.config import Settings
from app.services.llm_factory import get_llm


def test_get_llm_ollama():
    mock_ollama_cls = MagicMock()
    with patch(
        "app.services.llm_factory.settings",
        Settings(
            LLM_PROVIDER="ollama",
            OLLAMA_REQUEST_TIMEOUT=300.0,
            OLLAMA_KEEP_ALIVE="30m",
            OLLAMA_CONTEXT_WINDOW=4096,
        ),
    ), patch(
        "llama_index.llms.ollama.Ollama", mock_ollama_cls
    ):
        get_llm()
        mock_ollama_cls.assert_called_once_with(
            model="qwen2.5-coder:7b",
            base_url="http://ollama:11434",
            request_timeout=300.0,
            keep_alive="30m",
            context_window=4096,
        )


def test_get_llm_unknown_provider_raises():
    with patch("app.services.llm_factory.settings", Settings(LLM_PROVIDER="unknown")):
        with pytest.raises(ValueError, match="Unknown LLM provider"):
            get_llm()
