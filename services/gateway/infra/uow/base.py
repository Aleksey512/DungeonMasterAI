from abc import ABC, abstractmethod
from contextvars import ContextVar
from dataclasses import dataclass
from typing import Any

CURRENT_SESSION: ContextVar[Any | None] = ContextVar("CURRENT_SESSION", default=None)


@dataclass
class BaseUnitOfWork(ABC):
    async def __aenter__(self):
        await self.begin()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        if exc is None:
            await self.commit()
        else:
            await self.rollback()

    @abstractmethod
    async def begin(self):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...
