.PHONY: dev build test pull-models warm-embeddings

dev:
	docker compose up --build

build:
	docker compose build

test:
	cd backend && uv run pytest -v

pull-models:
	bash backend/scripts/pull_models.sh

warm-embeddings:
	docker compose exec backend python -c \
	  "from app.services.embedding_service import get_embed_model; get_embed_model(); print('Embedding model ready.')"
