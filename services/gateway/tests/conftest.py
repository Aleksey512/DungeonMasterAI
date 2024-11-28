# type:ignore
import pytest_asyncio
from gateway.infra.repositories.sqlalchemy.models import Base
from gateway.infra.uow.base import BaseUnitOfWork
from gateway.logic import TypedContainer
from gateway.logic.mediators.base import (
    BaseCommandMediator,
    BaseEventMediator,
    BaseMediator,
    BaseQueriesMediator,
)
from gateway.tests.fixtures import init_dummy_container
from pytest import fixture
from sqlalchemy.ext.asyncio import AsyncEngine


@pytest_asyncio.fixture(scope="function")
async def container() -> TypedContainer:
    container = init_dummy_container()
    engine = container.resolve(AsyncEngine)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return container


@fixture(scope="function")
def uow(container: TypedContainer) -> BaseUnitOfWork:
    return container.resolve(BaseUnitOfWork)


@fixture(scope="function")
def c_mediator(container: TypedContainer) -> BaseCommandMediator:
    return container.resolve(BaseCommandMediator)


@fixture(scope="function")
def q_mediator(container: TypedContainer) -> BaseQueriesMediator:
    return container.resolve(BaseQueriesMediator)


@fixture(scope="function")
def e_mediator(container: TypedContainer) -> BaseEventMediator:
    return container.resolve(BaseEventMediator)


@fixture(scope="function")
def mediator(container: TypedContainer) -> BaseMediator:
    return container.resolve(BaseMediator)
