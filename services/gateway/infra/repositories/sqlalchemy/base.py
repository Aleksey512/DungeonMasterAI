from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar

from gateway.domain.entities.base import BaseEntity
from gateway.infra.exceptions.repositories.sqlalchemy import SessionNotProvidedError
from gateway.infra.uow.base import CURRENT_SESSION
from sqlalchemy.ext.asyncio import AsyncSession

E = TypeVar("E", bound=BaseEntity)


@dataclass
class BaseSqlAlchemyRepository(ABC, Generic[E]):
    @property
    def session(self) -> AsyncSession:
        session: AsyncSession | None = CURRENT_SESSION.get()
        if session is None:
            raise SessionNotProvidedError()
        return session

    @abstractmethod
    def model_to_entity(self, model) -> E:
        ...
