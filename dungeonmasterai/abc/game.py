from abc import ABC, abstractmethod

from dungeonmasterai.abc.systems.base import System


class IGame(ABC):
    def __init__(self, *systems: System) -> None:
        self._systems: dict[type[System], System] = {
            s.__class__: s for s in sorted(systems, key=lambda s: s.priority)
        }

    @abstractmethod
    def start_session(self) -> None: ...

    @abstractmethod
    def end_session(self) -> None: ...
