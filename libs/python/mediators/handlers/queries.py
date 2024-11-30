from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Generic, TypeVar, cast

from mediators.handlers.base import BaseHandler
from mediators.registries.queries import QUERIES_HANDLER_REGISTRY

T = TypeVar("T")


@dataclass(frozen=True)
class BaseQuery(ABC, Generic[T]):
    limit: int = field(default=100, kw_only=True)
    offset: int = field(default=0, kw_only=True)


QT = TypeVar("QT", bound=BaseQuery)
QR = TypeVar("QR", bound=Any)


@dataclass()
class BaseQueryHandler(BaseHandler, Generic[QT, QR]):
    @abstractmethod
    async def handle(self, query: QT) -> QR:
        ...


def register_query_handler(handler: type[BaseQueryHandler]):
    def decorator(_class: type[QT]):
        QUERIES_HANDLER_REGISTRY.register(_class, handler)
        return cast(type[QT], _class)

    return decorator
