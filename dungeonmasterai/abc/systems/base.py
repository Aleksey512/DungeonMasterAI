from collections import defaultdict
from inspect import signature
from typing import Any, Callable


class System:
    def __init__(self, priority: int = 0) -> None:
        self._event_handlers: dict[str, list[Callable[..., None]]] = defaultdict(list)
        self.priority = priority

    def subscribe(self, event: str, handler: Callable[..., None]) -> None:
        self._event_handlers[event].append(handler)

    def unsubscribe(self, event: str, handler: Callable[..., None]) -> None:
        self._event_handlers[event].append(handler)

    def emit(self, event_type: str, *args: Any, **kwargs: Any) -> None:
        if event_type in self._event_handlers:
            for handler in self._event_handlers[event_type]:
                f_args, f_kwargs = self._filtered_args(handler, *args, **kwargs)
                handler(*f_args, **f_kwargs)

    def _filtered_args(
        self,
        method: Callable[..., None],
        *args: Any,
        **kwargs: Any,
    ) -> tuple[tuple[Any, ...], dict[str, Any]]:
        sig = signature(method)
        bound = sig.bind_partial(*args, **kwargs)
        bound.apply_defaults()
        return bound.args, bound.kwargs
