from dataclasses import dataclass

from gateway.logic.registries.base import BaseHandlersRegistry


@dataclass()
class CommandHandlersRegistry(BaseHandlersRegistry):
    ...


COMMAND_HANDLER_REGISTRY = CommandHandlersRegistry()
