from app.config import settings


def get_llm():
    provider = settings.LLM_PROVIDER
    if provider == "ollama":
        from llama_index.llms.ollama import Ollama

        return Ollama(model=settings.OLLAMA_MODEL, base_url=settings.OLLAMA_BASE_URL)
    if provider == "openai":
        from llama_index.llms.openai import OpenAI

        return OpenAI(model="gpt-4o", api_key=settings.OPENAI_API_KEY)
    if provider == "anthropic":
        from llama_index.llms.anthropic import Anthropic

        return Anthropic(model=settings.ANTHROPIC_MODEL, api_key=settings.ANTHROPIC_API_KEY)
    raise ValueError(f"Unknown LLM provider: {provider}")
