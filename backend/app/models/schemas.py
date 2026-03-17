from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str
    pipeline: str = "basic"
    session_id: str | None = None


class ChatResponse(BaseModel):
    response: str
    pipeline: str
    sources: list[dict] = Field(default_factory=list)
