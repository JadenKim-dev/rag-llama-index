#!/usr/bin/env bash
set -e

echo "Pulling Ollama models..."
docker compose exec ollama ollama pull qwen2.5-coder:7b
echo "Done."
