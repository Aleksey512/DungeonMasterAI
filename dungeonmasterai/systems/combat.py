from dungeonmasterai.abc.entities import IEntity
from dungeonmasterai.abc.events import Event, EventBus
from dungeonmasterai.abc.systems.character import CharacterEvents
from dungeonmasterai.abc.systems.combat import (
    ICombatSystem,
)


class CombatSystem(ICombatSystem):
    def __init__(self, e_bus: EventBus) -> None:
        super().__init__(e_bus)
        self._in_combat = False
        self._entities: set[IEntity] = set()

    def _on_start_commbat(self, *entities: IEntity) -> None:
        if self._in_combat:
            print("Combat Already Started")
            return
        if not entities:
            raise ValueError("Entities not provided")
        self._entities = set(e for e in entities)
        self._in_combat = True
        print(f"Combat started for {self._entities}")

    def _on_end_combat(self) -> None:
        if self._in_combat:
            self._entities = set()
            self._in_combat = False
        print("Combat ended")

    def _on_attack(self, attacker: IEntity, target: IEntity) -> None:
        if not self._in_combat:
            print("Combat not started")
            return
        if attacker not in self._entities:
            print("Attacker not in combat")
            return
        if target not in self._entities:
            print("Target not in combat")
            return
        print(f"{attacker} attack {target} for {attacker.attack} hp")
        self._e_bus.send_event(
            Event(
                name=CharacterEvents.character_take_damage,
                args=(
                    target,
                    attacker.attack,
                ),
                kwargs={},
            ),
        )
