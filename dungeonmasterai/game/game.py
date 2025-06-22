from dungeonmasterai.abc.events import EventBus
from dungeonmasterai.abc.game import IGame
from dungeonmasterai.abc.systems.base import System


class Game(IGame):
    def __init__(self, event_bus: EventBus, *systems: System) -> None:
        super().__init__(*systems)
        self.__event_bus: EventBus = event_bus

    def start_session(self) -> None:
        for event in self.__event_bus.listen():
            for system in self._systems.values():
                system.emit(event.name, *event.args, **event.kwargs)

    def end_session(self) -> None:
        self.__event_bus.stop()
