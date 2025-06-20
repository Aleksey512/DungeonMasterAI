from dataclasses import dataclass, field
from typing import Any, overload
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.player_managment.models import Player
from src.player_managment.schemas import PlayerCreate


@dataclass
class PlayerRepository:
    _session: AsyncSession | None = field(default=None)

    @property
    def session(self) -> AsyncSession:
        if not self._session:
            raise ValueError("Session not provided")
        return self._session

    @session.setter
    def session(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, player_data: PlayerCreate) -> Player:
        player = Player(**player_data.model_dump())
        self.session.add(player)
        return player

    @overload
    async def get(self, *, id: UUID) -> Player | None: ...

    @overload
    async def get(self, *, email: str) -> Player | None: ...

    async def get(self, *args: Any, **kwargs: Any) -> Player | None:
        if not kwargs:
            raise ValueError("Arguments not provided")
        stmt = select(Player).where(
            *[getattr(Player, k) == v for k, v in kwargs.items()]
        )
        result = await self.session.execute(stmt)
        return result.scalar()
