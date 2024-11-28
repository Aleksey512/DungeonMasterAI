from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from gateway.infra.uow.base import CURRENT_SESSION
from gateway.logic.commands.base import CommandHandler

if TYPE_CHECKING:
    from gateway.logic.commands.test.commands import SessionTestCommand  # noqa


@dataclass
class SessionTestCommandHandler(CommandHandler["SessionTestCommand", Any]):
    async def handle(self, command) -> Any:
        return CURRENT_SESSION.get()


@dataclass
class SessionTwoTestCommandHandler(CommandHandler["SessionTestCommand", Any]):
    async def handle(self, command) -> Any:
        return CURRENT_SESSION.get()
