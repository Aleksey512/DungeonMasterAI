from dataclasses import dataclass
from typing import TypeVar

from mediators.exceptions.mediators import EventHandlerNotRegisteredError
from mediators.handlers.events import ER, ET, BaseEvent, EventHandler
from mediators.mediators.base import BaseEventMediator

T = TypeVar("T")


@dataclass(eq=False)
class EventMediator(BaseEventMediator):
    def register_event(
        self,
        event: type[BaseEvent],
        event_handler: EventHandler[ET, ER],
    ):
        self.events_map[event].append(event_handler)

    async def handle_event(self, event: BaseEvent[T]) -> T:
        event_type = type(event)
        handlers = self.events_map.get(event_type)
        if not handlers:
            raise EventHandlerNotRegisteredError(event)

        result = tuple([await h.handle(event) for h in handlers])
        return result  # type:ignore
