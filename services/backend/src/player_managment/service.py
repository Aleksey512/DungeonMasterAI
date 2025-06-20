from dataclasses import dataclass
from uuid import UUID

from src.core.infra.database.session import sessionmaker
from src.player_managment.exceptions import (
    PlayerNotExistsError,
    PlayerWithThisEmailExistsError,
)
from src.player_managment.repository import PlayerRepository
from src.player_managment.schemas import PlayerCreate, PlayerResponse


@dataclass
class PlayerManagmentService:
    player_repo: PlayerRepository

    async def create_player(self, data: PlayerCreate) -> PlayerResponse:
        async with sessionmaker() as session:
            self.player_repo.session = session
            if await self.player_repo.get(email=data.email):
                raise PlayerWithThisEmailExistsError(data.email)
            player = await self.player_repo.create(data)
            await session.flush()
            await session.commit()
        return PlayerResponse.from_model(player)

    async def get_player_by_id(self, id: UUID) -> PlayerResponse:
        async with sessionmaker() as session:
            self.player_repo.session = session
            player = await self.player_repo.get(id=id)
            if not player:
                raise PlayerNotExistsError()
            return PlayerResponse.from_model(player)
