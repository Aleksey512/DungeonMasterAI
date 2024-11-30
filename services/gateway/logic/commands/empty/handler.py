from dataclasses import dataclass
from typing import TYPE_CHECKING

from mediators.handlers.commands.base import CommandHandler

if TYPE_CHECKING:
    from gateway.logic.commands.empty.command import EmptyCommand  # noqa


@dataclass()
class EmptyCommandHandler(CommandHandler["EmptyCommand", None]):
    async def handle(self, command):
        print(command.__doc__)


@dataclass()
class EmptyCommandHandler2(CommandHandler["EmptyCommand", int]):
    async def handle(self, command):
        print(command.x)
        return command.x
