import pytest
from httpx import ASGITransport, AsyncClient
from unittest.mock import AsyncMock, MagicMock, patch

from app.main import app


@pytest.mark.asyncio
async def test_chat_stub_returns_sse():
    pipeline = MagicMock()
    pipeline.aquery = AsyncMock(return_value={"response": "stubbed", "sources": []})
    with patch("app.api.routes.chat.get_pipeline", return_value=pipeline):
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
            async with client.stream("POST", "/api/chat", json={"message": "hello", "pipeline": "basic"}) as resp:
                assert resp.status_code == 200
                assert "text/event-stream" in resp.headers["content-type"]
                chunks = []
                async for line in resp.aiter_lines():
                    if line.startswith("data:"):
                        chunks.append(line)
                        break
                assert chunks
