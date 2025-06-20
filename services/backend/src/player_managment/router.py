from fastapi import APIRouter
from pydantic import UUID4

from core.dependencies import resolve_dependency
from src.player_managment.schemas import PlayerCreate, PlayerResponse
from src.player_managment.service import PlayerManagmentService

router = APIRouter(prefix="/players", tags=["Player"])


@router.get("/by_id/{id}", response_model=PlayerResponse)
async def get_by_id(
    id: UUID4,
    player_svc: PlayerManagmentService = resolve_dependency(PlayerManagmentService),
) -> PlayerResponse:
    return await player_svc.get_player_by_id(id)


@router.post("/create", response_model=PlayerResponse)
async def create_player(
    data: PlayerCreate,
    player_svc: PlayerManagmentService = resolve_dependency(PlayerManagmentService),
) -> PlayerResponse:
    return await player_svc.create_player(data)
