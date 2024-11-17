from abc import ABC, abstractmethod
from copy import copy
from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from uuid import uuid4

from gateway.domain.events.base import BaseEvent


@dataclass
class BaseEntity(ABC):
    """Base class for domain entities, providing common functionality like
    unique identifier generation, event registration, and equality comparison.

    Attributes:
        oid (str): Unique identifier for the entity, automatically generated
            using `uuid4` if not provided.
        created_at (datetime): Timestamp indicating when the entity was created
            Defaults to the current time if not provided.
        _events (list[BaseEvent]): List of events associated with the entity.
            Used for tracking changes or domain events.

    Methods:
        to_dict() -> dict:
            Abstract method that must be implemented by subclasses to return
            a dictionary representation of the entity.

        __hash__() -> int:
            Returns a hash value for the entity based on its `oid`.

        __eq__(value: BaseEntity) -> bool:
            Compares this entity with another based on their `oid`.

        register_event(event: BaseEvent) -> None:
            Registers a new domain event for the entity.

        pull_events() -> list[BaseEvent]:
            Retrieves and clears the list of registered domain events.
    """

    oid: str = field(default_factory=lambda: str(uuid4()), kw_only=True)
    created_at: datetime = field(default_factory=datetime.now, kw_only=True)
    _events: List[BaseEvent] = field(default_factory=list, kw_only=True)

    @abstractmethod
    def to_dict(self) -> dict:
        """Converts the entity to a dictionary representation. This method must
        be implemented by subclasses.

        Returns:
            dict: A dictionary representation of the entity.
        """

    def __hash__(self) -> int:
        """Returns a hash value for the entity, allowing it to be used in
        hashable collections like sets or as dictionary keys.

        Returns:
            int: The hash value based on the entity's `oid`.
        """
        return hash(self.oid)

    def __eq__(self, value: "BaseEntity") -> bool:  # type: ignore
        """Compares this entity with another for equality based on their unique
        identifier (`oid`).

        Args:
            value (BaseEntity): The entity to compare with.

        Returns:
            bool: `True` if the entities have the same `oid`, `False` otherwise.
        """
        return self.oid == value.oid

    def register_event(self, event: "BaseEvent") -> None:
        """Registers a new domain event for the entity.

        Args:
            event (BaseEvent): The event to register.
        """
        self._events.append(event)

    def pull_events(self) -> List["BaseEvent"]:
        """Retrieves all registered domain events and clears the event list.

        Returns:
            list[BaseEvent]: The list of registered events.
        """
        events = copy(self._events)
        self._events.clear()
        return events
