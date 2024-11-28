from dataclasses import dataclass

from gateway.domain.exceptions.base import ApplicationError


@dataclass(eq=False)
class BaseInfraError(ApplicationError):
    @property
    def message(self) -> str:
        return "Infra exception occured"
