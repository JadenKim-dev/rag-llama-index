import asyncio
from collections.abc import AsyncGenerator


async def text_to_sse(text: str, delay: float = 0.0) -> AsyncGenerator[str, None]:
    for char in text:
        yield f"event: token\ndata: {char}\n\n"
        await asyncio.sleep(delay)
    yield "event: done\ndata: [DONE]\n\n"
