from dataclasses import dataclass

from gateway.domain.exceptions.base import ApplicationError


@dataclass()
class LogicError(ApplicationError):
    @property
    def message(self) -> str:
        return "Base logic error"
