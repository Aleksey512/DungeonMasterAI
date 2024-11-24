from dataclasses import dataclass

from gateway.logic.registries.base import BaseHandlersRegistry


@dataclass()
class EventHandlersRegistry(BaseHandlersRegistry):
    ...


EVENTS_HANDLER_REGISTRY = EventHandlersRegistry()
