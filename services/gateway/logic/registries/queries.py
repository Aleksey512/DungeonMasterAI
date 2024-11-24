from dataclasses import dataclass

from gateway.logic.registries.base import BaseHandlersRegistry


@dataclass()
class QueriesHandlersRegistry(BaseHandlersRegistry):
    ...


QUERIES_HANDLER_REGISTRY = QueriesHandlersRegistry()
