from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.models.schemas import ChatRequest
from app.services.rag.pipeline_factory import get_pipeline
from app.utils.streaming import text_to_sse

router = APIRouter()


@router.post("/chat")
async def chat(request: ChatRequest) -> StreamingResponse:
    pipeline = await __import__("asyncio").to_thread(get_pipeline, request.pipeline)
    result = await pipeline.aquery(request.message)
    stub_response = result["response"]
    return StreamingResponse(
        text_to_sse(stub_response),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )
