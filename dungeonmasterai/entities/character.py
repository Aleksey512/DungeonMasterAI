from dataclasses import dataclass

from dungeonmasterai.abc.entities import IEntity


@dataclass()
class Character(IEntity):
    def __hash__(self) -> int:
        return hash(self._id)

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, IEntity):
            return False
        return self._id == value._id
