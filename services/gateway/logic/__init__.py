from functools import lru_cache
from typing import TypeVar

from gateway.infra.uow.base import BaseUnitOfWork
from gateway.infra.uow.sqlalchemy import SQLAlchemyUnitOfWork
from gateway.logic.mediator import AggregateMediator
from gateway.settings.config import Config
from mediators.mediators.base import (
    BaseCommandMediator,
    BaseEventMediator,
    BaseMediator,
    BaseQueriesMediator,
)
from mediators.mediators.commands import CommandMediator
from mediators.mediators.events import EventMediator
from mediators.mediators.queries import QueriesMediator
from mediators.registries.commands import COMMAND_HANDLER_REGISTRY
from mediators.registries.events import EVENTS_HANDLER_REGISTRY
from mediators.registries.queries import QUERIES_HANDLER_REGISTRY
from punq import Container, Scope
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

T = TypeVar("T")


class TypedContainer(Container):
    def resolve(self, service_key: type[T], **kwargs) -> T:
        return super().resolve(service_key, **kwargs)  # type:ignore


@lru_cache(1)
def init_container() -> TypedContainer:
    return _init_container()


def init_database(container: TypedContainer):
    config = container.resolve(Config)
    container.register(
        AsyncEngine,
        instance=create_async_engine(config.postgresql_url),
        scope=Scope.singleton,
    )
    container.register(
        async_sessionmaker,
        instance=async_sessionmaker(
            container.resolve(AsyncEngine),
            expire_on_commit=False,
            autoflush=False,
            autocommit=False,
        ),
    )

    def init_sesion() -> AsyncSession:
        return container.resolve(async_sessionmaker)()

    container.register(
        AsyncSession,
        factory=init_sesion,
    )


def init_unit_of_work(container: TypedContainer):
    container.register(BaseUnitOfWork, SQLAlchemyUnitOfWork)


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
    container.register(Config, instance=Config(), scope=Scope.singleton)  # type:ignore
    init_database(container)
    init_unit_of_work(container)
    init_command_mediator(container)
    init_event_mediator(container)
    init_query_mediator(container)

    container.register(BaseMediator, AggregateMediator)
    return container
