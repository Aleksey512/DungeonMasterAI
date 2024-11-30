from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar, cast

from mediators.handlers.base import BaseHandler
from mediators.registries.commands import COMMAND_HANDLER_REGISTRY

T = TypeVar("T")


@dataclass(frozen=True)
class BaseCommand(ABC, Generic[T]):
    ...


CT = TypeVar("CT", bound=BaseCommand)
CR = TypeVar("CR")


@dataclass()
class CommandHandler(BaseHandler, Generic[CT, CR]):
    @abstractmethod
    async def handle(self, command: CT) -> CR:
        ...


def register_command_handler(handler: type[CommandHandler]):
    def decorator(_class: type[CT]):
        COMMAND_HANDLER_REGISTRY.register(_class, handler)
        return cast(type[CT], _class)

    return decorator
