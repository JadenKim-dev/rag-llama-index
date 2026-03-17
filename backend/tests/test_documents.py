from unittest.mock import patch

import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_index_directory_not_found():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        resp = await client.post("/api/documents/index?directory=/nonexistent/path")
        assert resp.status_code == 404


@pytest.mark.asyncio
async def test_index_directory_success(tmp_path):
    (tmp_path / "sample.py").write_text("def hello(): pass")
    with patch("app.api.routes.documents.index_codebase", return_value=3):
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
            resp = await client.post(f"/api/documents/index?directory={tmp_path}")
            assert resp.status_code == 200
            assert resp.json()["indexed_chunks"] == 3
