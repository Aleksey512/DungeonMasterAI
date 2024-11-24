from dataclasses import dataclass
from typing import TypeVar

from gateway.logic.commands.base import CR, CT, BaseCommand, CommandHandler
from gateway.logic.exceptions.mediator import CommandHandlerNotRegisteredError
from gateway.logic.mediators.base import BaseCommandMediator

T = TypeVar("T")


@dataclass(eq=False)
class CommandMediator(BaseCommandMediator):
    def register_command(
        self,
        command: type[BaseCommand],
        command_handler: CommandHandler[CT, CR],
    ):
        self.commands_map[command].append(command_handler)

    async def handle_command(self, command: BaseCommand[T]) -> T:
        command_type = type(command)
        handlers = self.commands_map.get(command_type)

        if not handlers:
            raise CommandHandlerNotRegisteredError(command)

        results = tuple([await h.handle(command) for h in handlers])

        return results  # type:ignore
