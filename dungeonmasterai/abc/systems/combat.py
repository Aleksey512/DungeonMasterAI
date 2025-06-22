from abc import ABC, abstractmethod

from dungeonmasterai.abc.entities import IEntity
from dungeonmasterai.abc.systems.base import System


class ICombatSystem(System, ABC):
    def __init__(self) -> None:
        super().__init__()
        self.subscribe("START_COMBAT", self._on_start_commbat)
        self.subscribe("END_COMBAT", self._on_end_combat)
        self.subscribe("ATTACK", self._on_attack)

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
