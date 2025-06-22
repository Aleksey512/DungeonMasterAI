from abc import ABC, abstractmethod
from typing import Any, Generator, Generic, TypeVar

from pydantic import BaseModel, ConfigDict

TArgs = TypeVar("TArgs", bound=tuple[Any, ...])
TKwargs = TypeVar("TKwargs", bound=dict[str, Any])


class Event(BaseModel, Generic[TArgs, TKwargs]):
    name: str
    args: TArgs
    kwargs: TKwargs
    model_config = ConfigDict(arbitrary_types_allowed=True)


class EventBus(ABC):
    @abstractmethod
    def send_event(self, event: Event[tuple[Any, ...], dict[str, Any]]) -> None: ...

    @abstractmethod
    def listen(
        self,
    ) -> Generator[Event[tuple[Any, ...], dict[str, Any]], None, None]: ...

    @abstractmethod
    def stop(self) -> None: ...
