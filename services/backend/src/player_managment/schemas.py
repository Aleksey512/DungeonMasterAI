from typing import Self
from uuid import UUID

from pydantic import BaseModel, EmailStr
from src.player_managment.models import Player


class PlayerCreate(BaseModel):
    name: str
    email: EmailStr


class PlayerResponse(BaseModel):
    id: UUID
    name: str

    @classmethod
    def from_model(cls, model: Player) -> Self:
        return cls(id=model.id, name=model.name)
