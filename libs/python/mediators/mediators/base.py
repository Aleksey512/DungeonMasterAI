from abc import ABC, abstractmethod
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any, Protocol, TypeVar

from mediators.handlers.commands import CR, CT, BaseCommand, CommandHandler
from mediators.handlers.events import ER, ET, BaseEvent, EventHandler
from mediators.handlers.queries import QR, QT, BaseQuery, BaseQueryHandler

T = TypeVar("T", bound=Any)


class BaseMediator(Protocol):
    def register_command(
        self,
        command: type[BaseCommand],
        command_handler: CommandHandler[CT, CR],
    ):
        ...

    async def handle_command(self, command: BaseCommand[T]) -> T:
        ...

    def register_event(
        self,
        event: type[BaseEvent],
        event_handler: EventHandler[ET, ER],
    ):
        ...

    async def handle_event(self, event: BaseEvent[T]) -> T:
        ...

    def register_query(
        self,
        query: type[BaseQuery],
        query_handler: BaseQueryHandler[QT, QR],
    ):
        ...

    async def handle_query(self, query: BaseQuery[T]) -> T:
        ...


@dataclass(eq=False)
class BaseCommandMediator(ABC):
    commands_map: dict[type[BaseCommand], list[CommandHandler[Any, Any]]] = field(
        default_factory=lambda: defaultdict(list), kw_only=True
    )

    @abstractmethod
    def register_command(
        self,
        command: type[BaseCommand],
        command_handler: CommandHandler[CT, CR],
    ):
        ...

    @abstractmethod
    async def handle_command(self, command: BaseCommand[T]) -> T:
        ...


@dataclass(eq=False)
class BaseEventMediator(ABC):
    events_map: dict[type[BaseEvent], list[EventHandler]] = field(
        default_factory=lambda: defaultdict(list), kw_only=True
    )

    @abstractmethod
    def register_event(
        self,
        event: type[BaseEvent],
        event_handler: EventHandler[ET, ER],
    ):
        ...

    @abstractmethod
    async def handle_event(self, event: BaseEvent[T]) -> T:
        ...


@dataclass(eq=False)
class BaseQueriesMediator(ABC):
    queries_map: dict[type[BaseQuery], list[BaseQueryHandler]] = field(
        default_factory=lambda: defaultdict(list), kw_only=True
    )

    @abstractmethod
    def register_query(
        self,
        query: type[BaseQuery],
        query_handler: BaseQueryHandler[QT, QR],
    ):
        ...

    @abstractmethod
    async def handle_query(self, query: BaseQuery[T]) -> T:
        ...
