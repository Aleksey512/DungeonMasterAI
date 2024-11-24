from abc import ABC
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Generic, TypeVar

C = TypeVar("C")
CH = TypeVar("CH")


@dataclass
class BaseHandlersRegistry(ABC, Generic[C, CH]):
    _registry: dict[type[C], list[type[CH]]] = field(
        default_factory=lambda: defaultdict(list), kw_only=True
    )

    @property
    def registry(self) -> dict[type[C], list[type[CH]]]:
        return self._registry

    def register(self, _class: type[C], handler_class: type[CH]):
        self.registry[_class].append(handler_class)
