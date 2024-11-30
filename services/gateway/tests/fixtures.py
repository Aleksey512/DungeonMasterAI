from gateway.logic import (
    TypedContainer,
    init_command_mediator,
    init_event_mediator,
    init_query_mediator,
    init_unit_of_work,
)
from gateway.logic.mediator import AggregateMediator
from gateway.settings.config import Config
from mediators.mediators.base import BaseMediator
from punq import Scope
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)


def _init_mock_database(container: TypedContainer):
    def init_engine() -> AsyncEngine:
        return create_async_engine(
            "sqlite+aiosqlite:///:memory:",
            echo=False,
            future=True,
        )

    container.register(
        AsyncEngine,
        factory=init_engine,
        scope=Scope.singleton,
    )

    def init_sessionmaker() -> async_sessionmaker:
        return async_sessionmaker(
            container.resolve(AsyncEngine),
            expire_on_commit=False,
            autoflush=False,
            autocommit=False,
        )

    container.register(
        async_sessionmaker,
        factory=init_sessionmaker,
        scope=Scope.singleton,
    )

    def init_sesion() -> AsyncSession:
        return container.resolve(async_sessionmaker)()

    container.register(
        AsyncSession,
        factory=init_sesion,
    )


def init_dummy_container() -> TypedContainer:
    container = TypedContainer()

    # CONFIG
    container.register(
        Config, instance=Config(), scope=Scope.singleton  # type:ignore
    )

    _init_mock_database(container)
    init_unit_of_work(container)

    init_event_mediator(container)
    init_query_mediator(container)
    init_command_mediator(container)

    container.register(BaseMediator, AggregateMediator)
    return container
