from dataclasses import dataclass

from gateway.infra.uow.base import CURRENT_SESSION, BaseUnitOfWork
from sqlalchemy.ext.asyncio import AsyncSession


@dataclass
class SQLAlchemyUnitOfWork(BaseUnitOfWork):
    _session: AsyncSession

    async def begin(self):
        if not self._session.is_active:
            await self._session.begin()
        self.token = CURRENT_SESSION.set(self._session)

    async def commit(self):
        try:
            if self._session.is_active:
                await self._session.commit()
        finally:
            CURRENT_SESSION.reset(self.token)

    async def rollback(self):
        try:
            if self._session.is_active:
                await self._session.rollback()
        finally:
            CURRENT_SESSION.reset(self.token)
