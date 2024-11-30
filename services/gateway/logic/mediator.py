from dataclasses import dataclass
from typing import TypeVar

from gateway.infra.uow.base import BaseUnitOfWork
from mediators.handlers.commands import CR, CT, BaseCommand, CommandHandler
from mediators.handlers.events import ER, ET, BaseEvent, EventHandler
from mediators.handlers.queries import QR, QT, BaseQuery, BaseQueryHandler
from mediators.mediators.base import (
    BaseCommandMediator,
    BaseEventMediator,
    BaseQueriesMediator,
)

T = TypeVar("T")


@dataclass(eq=False)
class AggregateMediator:
    _queries_mediator: BaseQueriesMediator
    _commands_mediator: BaseCommandMediator
    _events_mediator: BaseEventMediator
    _unit_of_work: BaseUnitOfWork

    def register_command(
        self,
        command: type[BaseCommand],
        command_handler: CommandHandler[CT, CR],
    ):
        self._commands_mediator.register_command(command, command_handler)

    async def handle_command(self, command: BaseCommand[T]) -> T:
        async with self._unit_of_work:
            return await self._commands_mediator.handle_command(command)

    def register_event(
        self,
        event: type[BaseEvent],
        event_handler: EventHandler[ET, ER],
    ):
        self._events_mediator.register_event(event, event_handler)

    async def handle_event(self, event: BaseEvent[T]) -> T:
        async with self._unit_of_work:
            return await self._events_mediator.handle_event(event)

    def register_query(
        self,
        query: type[BaseQuery],
        query_handler: BaseQueryHandler[QT, QR],
    ):
        self._queries_mediator.register_query(query, query_handler)

    async def handle_query(self, query: BaseQuery[T]) -> T:
        async with self._unit_of_work:
            return await self.handle_query(query)
