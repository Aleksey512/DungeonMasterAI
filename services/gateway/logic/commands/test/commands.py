from dataclasses import dataclass
from typing import Any

from gateway.logic.commands.base import BaseCommand, register_command_handler
from gateway.logic.commands.test.handlers import (
    SessionTestCommandHandler,
    SessionTwoTestCommandHandler,
)


@register_command_handler(SessionTwoTestCommandHandler)
@register_command_handler(SessionTestCommandHandler)
@dataclass(frozen=True)
class SessionTestCommand(BaseCommand[tuple[Any, Any]]):
    ...
