from dungeonmasterai.abc.events import Event
from dungeonmasterai.abc.systems.character import CharacterEvents
from dungeonmasterai.abc.systems.combat import CombatEvents
from dungeonmasterai.entities.character import Character
from dungeonmasterai.event_bus.queue import QueueEventBus
from dungeonmasterai.game.game import Game
from dungeonmasterai.systems.character import CharacterSystem
from dungeonmasterai.systems.combat import CombatSystem


def main() -> None:
    ebus = QueueEventBus(maxsize=10)
    combat_system = CombatSystem(ebus)
    character_system = CharacterSystem(ebus)
    char_1 = Character(100, 1, 99)
    char_2 = Character(100, 1, 2)
    character_system.emit(CharacterEvents.characted_craeted, char_1)
    character_system.emit(CharacterEvents.characted_craeted, char_2)
    game = Game(ebus, combat_system, character_system)
    game.start_session()
    try:
        ebus.send_event(
            Event(name=CombatEvents.start_combat, args=(char_1, char_2), kwargs={}),
        )
        ebus.send_event(
            Event(name=CombatEvents.attack, args=(char_1, char_2), kwargs={}),
        )
        ebus.send_event(Event(name=CombatEvents.end_combat, args=(), kwargs={}))
        while True:
            ...
    except KeyboardInterrupt:
        print("Stopping game")
    finally:
        game.end_session()
        print("Game session ended")


if __name__ == "__main__":
    main()
