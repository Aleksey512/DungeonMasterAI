from abc import ABC, abstractmethod

from dungeonmasterai.abc.entities import IEntity
from dungeonmasterai.abc.events import EventBus
from dungeonmasterai.abc.systems.base import System


class CombatEvents:
    start_combat = "START_COMBAT"
    end_combat = "END_COMBAT"
    attack = "ATTACK"


class ICombatSystem(System, ABC):
    def __init__(self, e_bus: EventBus) -> None:
        super().__init__(e_bus)
        self.subscribe(CombatEvents.start_combat, self._on_start_commbat)
        self.subscribe(CombatEvents.end_combat, self._on_end_combat)
        self.subscribe(CombatEvents.attack, self._on_attack)

    @abstractmethod
    def _on_start_commbat(self, *entities: IEntity) -> None: ...

    @abstractmethod
    def _on_end_combat(self) -> None: ...

    @abstractmethod
    def _on_attack(
        self,
        attacker: IEntity,
        target: IEntity,
    ) -> None: ...
