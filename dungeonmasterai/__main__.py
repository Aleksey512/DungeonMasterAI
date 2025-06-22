import threading
import time

from dungeonmasterai.abc.events import Event
from dungeonmasterai.entities.character import Character
from dungeonmasterai.event_bus.queue import QueueEventBus
from dungeonmasterai.game.game import Game
from dungeonmasterai.systems.combat import CombatSystem

ebus = QueueEventBus(maxsize=10)
combat_system = CombatSystem()

game = Game(ebus, combat_system)


def main() -> None:
    thread = threading.Thread(target=game.start_session)
    thread.start()
    char_1 = Character()
    char_2 = Character()
    ebus.send_event(Event(name="START_COMBAT", args=(char_1, char_2), kwargs={}))
    ebus.send_event(Event(name="ATTACK", args=(char_1, char_2), kwargs={}))
    ebus.send_event(Event(name="ATTACK", args=(char_1, char_2), kwargs={}))
    ebus.send_event(Event(name="END_COMBAT", args=(), kwargs={}))
    time.sleep(5)
    ebus.stop()
    thread.join()


if __name__ == "__main__":
    main()
