from dataclasses import dataclass

from gateway.infra.exceptions.base import BaseInfraError


@dataclass(eq=False)
class SessionNotProvidedError(BaseInfraError):
    @property
    def message(self):
        return "Session not provided to repository"
