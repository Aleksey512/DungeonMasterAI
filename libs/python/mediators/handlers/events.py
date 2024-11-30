from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Generic, TypeVar, cast

from mediators.handlers.base import BaseHandler
from mediators.registries.events import EVENTS_HANDLER_REGISTRY

T = TypeVar("T")


@dataclass(frozen=True)
class BaseEvent(ABC, Generic[T]):
    @abstractmethod
    def get_key(self) -> bytes:
        ...


ET = TypeVar("ET", bound=BaseEvent)
ER = TypeVar("ER", bound=Any)


@dataclass
class EventHandler(BaseHandler, Generic[ET, ER]):
    @abstractmethod
    async def handle(self, event: ET) -> ER:
        ...


def register_event_handler(handler: type[EventHandler]):
    def decorator(_class: type[ET]):
        EVENTS_HANDLER_REGISTRY.register(_class, handler)
        return cast(type[ET], _class)

    return decorator
