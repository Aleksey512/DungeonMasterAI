import queue
import threading
from contextlib import suppress
from typing import Any, Generator

from dungeonmasterai.abc.events import Event, EventBus


class QueueEventBus(EventBus):
    """
    Реализация EventBus c поддержкой множества слушателей.
    Каждый слушатель получает копию события.
    """

    def __init__(self, maxsize: int = 0) -> None:
        self._listeners: list[queue.Queue[Event]] = []
        self._lock = threading.Lock()
        self._maxsize = maxsize
        self._stop_event = threading.Event()

    def send_event(self, event: Event[tuple[Any, ...], dict[str, Any]]) -> None:
        """Отправляет событие всем слушателям."""
        with self._lock:
            for listener_queue in self._listeners:
                try:
                    listener_queue.put(event.model_copy())
                except queue.Full:
                    continue

    def listen(self) -> Generator[Event[tuple[Any, ...], dict[str, Any]], None, None]:
        """Создает новый слушатель событий."""
        listener_queue = queue.Queue[Event](maxsize=self._maxsize)
        with self._lock:
            self._listeners.append(listener_queue)

        try:
            while not self._stop_event.is_set():
                try:
                    event = listener_queue.get(timeout=0.1)
                    yield event
                    listener_queue.task_done()
                except queue.Empty:
                    continue
        finally:
            with self._lock:
                self._listeners.remove(listener_queue)

    def stop(self) -> None:
        """Останавливает все слушатели."""
        self._stop_event.set()
        with self._lock, suppress(queue.Full):
            for listener_queue in self._listeners:
                listener_queue.put(Event(name="", args=(), kwargs={}))
