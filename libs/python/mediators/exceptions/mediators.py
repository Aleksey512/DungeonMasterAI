from dataclasses import dataclass

from mediators.exceptions.base import MediatorsError
from mediators.handlers.commands import BaseCommand
from mediators.handlers.events import BaseEvent
from mediators.handlers.queries import BaseQuery


@dataclass()
class CommandHandlerNotRegisteredError(MediatorsError):
    command: BaseCommand

    @property
    def message(self) -> str:
        return f"No one handler found {self.command}"


@dataclass()
class EventHandlerNotRegisteredError(MediatorsError):
    event: BaseEvent

    @property
    def message(self) -> str:
        return f"No one handler found for {self.event}"


@dataclass()
class QueryHandlerNotRegisteredError(MediatorsError):
    query: BaseQuery

    @property
    def message(self) -> str:
        return f"No one handler found for {self.query}"
