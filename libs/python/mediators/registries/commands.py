from dataclasses import dataclass

from mediators.registries.base import BaseHandlersRegistry


@dataclass()
class CommandHandlersRegistry(BaseHandlersRegistry):
    ...


COMMAND_HANDLER_REGISTRY = CommandHandlersRegistry()
