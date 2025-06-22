from abc import ABC, abstractmethod

from dungeonmasterai.abc.entities import IEntity
from dungeonmasterai.abc.events import EventBus
from dungeonmasterai.abc.systems.base import System


class CharacterEvents:
    characted_craeted = "CHARACTER_CREATED"
    character_take_damage = "CHARACTER_TAKE_DAMAGE"
    character_died = "CHARACTER_DIED"


class ICharacterSystem(System, ABC):
    def __init__(self, e_bus: EventBus, priority: int = 0) -> None:
        super().__init__(e_bus, priority)
        self.subscribe(CharacterEvents.character_take_damage, self._on_char_take_dmg)
        self.subscribe(CharacterEvents.character_died, self._on_char_died)
        self.subscribe(CharacterEvents.characted_craeted, self._on_char_created)

    @abstractmethod
    def _on_char_take_dmg(self, entity: IEntity, dmg: int) -> None: ...

    @abstractmethod
    def _on_char_died(self, entity: IEntity) -> None: ...

    @abstractmethod
    def _on_char_created(self, entity: IEntity) -> None: ...
