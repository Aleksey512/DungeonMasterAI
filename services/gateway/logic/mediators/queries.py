from dataclasses import dataclass
from typing import Any, TypeVar

from gateway.logic.exceptions.mediator import QueryHandlerNotRegisteredError
from gateway.logic.mediators.base import BaseQueriesMediator
from gateway.logic.queries.base import QR, QT, BaseQuery, BaseQueryHandler

T = TypeVar("T", bound=Any)


@dataclass(eq=False)
class QueriesMediator(BaseQueriesMediator):
    def register_query(
        self,
        query: type[BaseQuery],
        query_handler: BaseQueryHandler[QT, QR],
    ):
        self.queries_map[query].append(query_handler)

    async def handle_query(self, query: BaseQuery[T]) -> T:
        query_type = type(query)
        handlers = self.queries_map.get(query_type)

        if not handlers:
            raise QueryHandlerNotRegisteredError(query)

        result = tuple([await h.handle(query) for h in handlers])

        return result  # type:ignore
