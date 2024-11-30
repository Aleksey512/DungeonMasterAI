from dataclasses import dataclass

from mediators.registries.base import BaseHandlersRegistry


@dataclass()
class QueriesHandlersRegistry(BaseHandlersRegistry):
    ...


QUERIES_HANDLER_REGISTRY = QueriesHandlersRegistry()
