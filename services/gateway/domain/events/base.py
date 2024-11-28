import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import ClassVar, Generic, TypeVar

T = TypeVar("T")


@dataclass
class BaseEvent(ABC, Generic[T]):

    """Abstract base class for domain events.

    This class provides a template for defining domain events with a unique
    identifier and a static `event_name`. Subclasses must implement the
    `get_key` method to define the event's unique key.

    Attributes:
        event_name (ClassVar[str]): A class-level attribute that defines the
            name of the event. This should be set in subclasses.
        event_id (uuid.UUID): A unique identifier for the event, automatically
            generated if not provided.

    Methods:
        get_key() -> bytes:
            Abstract method to return a unique key representing the event.
            Must be implemented by subclasses.

    Examples:
        Defining a custom event:
            >>> from typing import ClassVar
            >>> class UserCreatedEvent(BaseEvent):
            ...     event_name: ClassVar[str] = "user_created"
            ...
            ...     def get_key(self) -> bytes:
            ...         return self.event_id.bytes

        Creating and using the event:
            >>> event = UserCreatedEvent()
            >>> print(event.event_name)  # Output: user_created
            >>> print(event.event_id)    # Output: A unique UUID
            >>> print(event.get_key())   # Output: UUID as bytes
    """

    event_name: ClassVar[str]

    event_id: uuid.UUID = field(default_factory=uuid.uuid4, kw_only=True)

    @abstractmethod
    def get_key(self) -> bytes:
        """Abstract method to return a unique key representing the event.

        This method must be implemented by subclasses to define the
        specific key representation for the event.

        Returns:
            bytes: A byte sequence representing the event's unique key.
        """
