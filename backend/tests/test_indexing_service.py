from unittest.mock import MagicMock, mock_open, patch

from app.services.indexing_service import index_codebase


def test_index_codebase_uses_storage_context_for_vector_store(tmp_path):
    source_file = tmp_path / "sample.py"
    source_file.write_text("def chat(): pass")

    node = MagicMock()
    node.text = "def chat(): pass"
    node.metadata = {"file_path": str(source_file), "language": "python"}

    mock_collection = MagicMock()
    mock_client = MagicMock()
    mock_client.get_or_create_collection.return_value = mock_collection
    mock_storage_context = object()

    with patch("app.services.indexing_service.get_embed_model", return_value=object()), patch(
        "app.services.indexing_service.get_code_nodes", return_value=[node]
    ), patch("app.services.indexing_service.enrich_nodes", return_value=[node]), patch(
        "app.services.indexing_service.chromadb.PersistentClient", return_value=mock_client
    ), patch(
        "app.services.indexing_service.ChromaVectorStore", return_value="vector-store"
    ), patch(
        "app.services.indexing_service.StorageContext.from_defaults",
        return_value=mock_storage_context,
    ) as mock_storage_from_defaults, patch(
        "app.services.indexing_service.VectorStoreIndex"
    ) as mock_index, patch(
        "app.services.indexing_service.open", mock_open()
    ), patch(
        "app.services.indexing_service.pickle.dump"
    ):
        count = index_codebase(str(tmp_path))

    assert count == 1
    mock_storage_from_defaults.assert_called_once_with(vector_store="vector-store")
    mock_index.assert_called_once_with(nodes=[node], storage_context=mock_storage_context)
