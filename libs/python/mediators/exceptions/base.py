from dataclasses import dataclass


@dataclass()
class MediatorsError(Exception):
    @property
    def message(self) -> str:
        return "Base mediators error"
