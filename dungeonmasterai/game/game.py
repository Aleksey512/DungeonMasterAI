from threading import Thread

from dungeonmasterai.abc.events import EventBus
from dungeonmasterai.abc.game import IGame
from dungeonmasterai.abc.systems.base import System


class Game(IGame):
    def __init__(self, event_bus: EventBus, *systems: System) -> None:
        super().__init__(*systems)
        self.__event_bus: EventBus = event_bus
        self.__threads: list[Thread] = []

    def start_session(self) -> None:
        for system in self._systems.values():
            thr = Thread(target=system.listen)
            self.__threads.append(thr)
            thr.start()

    def end_session(self) -> None:
        self.__event_bus.stop()
        for thr in self.__threads:
            thr.join()
