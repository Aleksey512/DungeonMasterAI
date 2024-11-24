from dataclasses import dataclass, field

from gateway.logic.commands.base import BaseCommand, register_command_handler
from gateway.logic.commands.empty.handler import (
    EmptyCommandHandler,
    EmptyCommandHandler2,
)


@register_command_handler(EmptyCommandHandler2)
@register_command_handler(EmptyCommandHandler)
@dataclass(frozen=True)
class EmptyCommand(BaseCommand[tuple[None, int]]):
    x: int = field(default=1, kw_only=True)
