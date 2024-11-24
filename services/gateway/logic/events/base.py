from abc import abstractmethod
from dataclasses import dataclass
from typing import Any, Generic, TypeVar, cast

from gateway.domain.events.base import BaseEvent
from gateway.logic.base import BaseHandler
from gateway.logic.registries.events import EVENTS_HANDLER_REGISTRY

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
