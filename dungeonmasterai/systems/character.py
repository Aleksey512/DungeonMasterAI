from dungeonmasterai.abc.entities import IEntity
from dungeonmasterai.abc.events import Event, EventBus
from dungeonmasterai.abc.systems.character import CharacterEvents, ICharacterSystem


class CharacterSystem(ICharacterSystem):
    def __init__(self, e_bus: EventBus, priority: int = 0) -> None:
        super().__init__(e_bus, priority)
        self._characters: set[IEntity] = set()

    def _on_char_created(self, entity: IEntity) -> None:
        print(f"Character added {entity}")
        self._characters.add(entity)

    def _on_char_died(self, entity: IEntity) -> None:
        if entity in self._characters:
            print(f"Character {entity} died")
            self._characters.remove(entity)

    def _on_char_take_dmg(self, entity: IEntity, dmg: int) -> None:
        if entity not in self._characters:
            print(f"Character {entity} not exists")
            return
        entity.hp -= dmg
        if entity.hp <= 0:
            self._e_bus.send_event(
                Event(name=CharacterEvents.character_died, args=(entity,), kwargs={}),
            )
