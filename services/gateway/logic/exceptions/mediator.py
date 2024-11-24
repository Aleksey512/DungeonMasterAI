from dataclasses import dataclass

from gateway.domain.events.base import BaseEvent
from gateway.logic.commands.base import BaseCommand
from gateway.logic.exceptions.base import LogicError
from gateway.logic.queries.base import BaseQuery


@dataclass()
class CommandHandlerNotRegisteredError(LogicError):
    command: BaseCommand

    @property
    def message(self) -> str:
        return f"No one handler found {self.command}"


@dataclass()
class EventHandlerNotRegisteredError(LogicError):
    event: BaseEvent

    @property
    def message(self) -> str:
        return f"No one handler found for {self.event}"


@dataclass()
class QueryHandlerNotRegisteredError(LogicError):
    query: BaseQuery

    @property
    def message(self) -> str:
        return f"No one handler found for {self.query}"
