from dataclasses import dataclass, field
from uuid import uuid4


@dataclass()
class IEntity:
    hp: int
    armor: int
    attack: int
    _id: str = field(default_factory=lambda: uuid4().hex)

    def __hash__(self) -> int:
        return hash(self._id)

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, IEntity):
            return False
        return self._id == value._id
