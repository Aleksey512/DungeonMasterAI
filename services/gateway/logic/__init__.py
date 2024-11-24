from functools import lru_cache
from typing import TypeVar

from gateway.logic.mediator import AggregateMediator
from gateway.logic.mediators.base import (
    BaseCommandMediator,
    BaseEventMediator,
    BaseMediator,
    BaseQueriesMediator,
)
from gateway.logic.mediators.commands import CommandMediator
from gateway.logic.mediators.events import EventMediator
from gateway.logic.mediators.queries import QueriesMediator
from gateway.logic.registries.commands import COMMAND_HANDLER_REGISTRY
from gateway.logic.registries.events import EVENTS_HANDLER_REGISTRY
from gateway.logic.registries.queries import QUERIES_HANDLER_REGISTRY
from punq import Container

T = TypeVar("T")


class TypedContainer(Container):
    def resolve(self, service_key: type[T], **kwargs) -> T:
        return super().resolve(service_key, **kwargs)  # type:ignore


@lru_cache(1)
def init_container() -> TypedContainer:
    return _init_container()


def init_command_mediator(container: TypedContainer):
    def f() -> BaseCommandMediator:
        mediator = CommandMediator()
        for command, handlers in COMMAND_HANDLER_REGISTRY.registry.items():
            for h in handlers:
                container.register(h)
                mediator.register_command(command, container.resolve(h))
        return mediator

    container.register(BaseCommandMediator, factory=f)


def init_event_mediator(container: TypedContainer):
    def f() -> BaseEventMediator:
        mediator = EventMediator()
        for event, handlers in EVENTS_HANDLER_REGISTRY.registry.items():
            for h in handlers:
                container.register(h)
                mediator.register_event(event, container.resolve(h))
        return mediator

    container.register(BaseEventMediator, factory=f)


def init_query_mediator(container: TypedContainer):
    def f() -> BaseQueriesMediator:
        mediator = QueriesMediator()
        for query, handlers in QUERIES_HANDLER_REGISTRY.registry.items():
            for h in handlers:
                container.register(h)
                mediator.register_query(query, container.resolve(h))
        return mediator

    container.register(BaseQueriesMediator, factory=f)


def _init_container() -> TypedContainer:
    container = TypedContainer()
    init_command_mediator(container)
    init_event_mediator(container)
    init_query_mediator(container)

    container.register(BaseMediator, AggregateMediator)
    return container
