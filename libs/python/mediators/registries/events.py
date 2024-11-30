from dataclasses import dataclass

from mediators.registries.base import BaseHandlersRegistry


@dataclass()
class EventHandlersRegistry(BaseHandlersRegistry):
    ...


EVENTS_HANDLER_REGISTRY = EventHandlersRegistry()
