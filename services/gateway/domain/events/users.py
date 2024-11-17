from dataclasses import dataclass
from typing import ClassVar

from gateway.domain.events.base import BaseEvent
from gateway.settings.const import USER_CREATED_EVENT_NAME


@dataclass
class UserCreatedEvent(BaseEvent):
    event_name: ClassVar[str] = USER_CREATED_EVENT_NAME

    email: str

    def get_key(self) -> bytes:
        return self.email.encode()
