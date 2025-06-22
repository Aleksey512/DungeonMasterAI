import queue
import threading
from typing import Any, Generator

from dungeonmasterai.abc.events import Event, EventBus


class QueueEventBus(EventBus):
    """
    Реализация EventBus на основе очереди (thread-safe).
    - send_event() добавляет событие в очередь
    - listen() бесконечно возвращает события из очереди
    """

    def __init__(self, maxsize: int = 0) -> None:
        self._queue = queue.Queue[Event[tuple[Any, ...], dict[str, Any]]](
            maxsize=maxsize,
        )
        self._stop_event = threading.Event()

    def send_event(self, event: Event[tuple[Any, ...], dict[str, Any]]) -> None:
        self._queue.put(event)

    def listen(self) -> Generator[Event[tuple[Any, ...], dict[str, Any]], None, None]:
        while not self._stop_event.is_set():
            try:
                event = self._queue.get()
                yield event
            except queue.Empty:
                continue

    def stop(self) -> None:
        self._stop_event.set()
        self._queue.put(Event(name="", args=(), kwargs={}))
