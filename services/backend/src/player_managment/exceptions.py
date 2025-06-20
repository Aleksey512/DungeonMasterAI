from dataclasses import dataclass

from src.core.exceptions.base import BaseError


@dataclass(eq=False, frozen=True)
class PlayerWithThisEmailExistsError(BaseError):
    email: str

    @property
    def message(self) -> str:
        return f"Player with {self.email} already exists"


@dataclass(eq=False, frozen=True)
class PlayerNotExistsError(BaseError):
    @property
    def message(self) -> str:
        return "Player not exists"
