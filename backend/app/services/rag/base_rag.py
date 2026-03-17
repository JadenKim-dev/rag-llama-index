from abc import ABC, abstractmethod
import asyncio


class BaseRAGService(ABC):
    @abstractmethod
    def query(self, question: str) -> dict:
        raise NotImplementedError

    async def aquery(self, question: str) -> dict:
        return await asyncio.to_thread(self.query, question)
