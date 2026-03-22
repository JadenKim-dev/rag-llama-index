from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # LLM
    LLM_PROVIDER: str = "ollama"
    OLLAMA_MODEL: str = "qwen2.5-coder:7b"
    OLLAMA_BASE_URL: str = "http://ollama:11434"
    OLLAMA_REQUEST_TIMEOUT: float = 300.0
    OLLAMA_KEEP_ALIVE: str = "30m"
    OLLAMA_CONTEXT_WINDOW: int = 4096
    OPENAI_API_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""
    ANTHROPIC_MODEL: str = "claude-sonnet-4-5"

    # Embedding
    EMBED_DEVICE: str = "cpu"

    # Vector Store
    VECTOR_STORE_PATH: str = "./storage"
    CHROMA_COLLECTION: str = "code_index"

    # Qdrant (Phase 2+)
    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333


settings = Settings()
