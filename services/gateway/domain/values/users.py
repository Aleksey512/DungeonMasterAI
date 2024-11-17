import re
from dataclasses import dataclass

from gateway.domain.exceptions.users import InvalidEmailError, InvalidPasswordError
from gateway.domain.values.base import BaseValueObject
from gateway.settings.const import EMAIL_MASK, PASS_MASK


@dataclass(frozen=True, eq=False)
class Email(BaseValueObject[str]):
    def validate(self):
        if not re.match(EMAIL_MASK, self.value):
            raise InvalidEmailError(self.value)

    def as_generic_type(self) -> str:
        return str(self.value)


@dataclass(frozen=True, eq=False)
class CleanPassword(BaseValueObject[str]):
    def validate(self):
        if not re.match(PASS_MASK, self.value):
            raise InvalidPasswordError(self.value)

    def as_generic_type(self) -> str:
        return str(self.value)


@dataclass(frozen=True, eq=False)
class HashablePassword(BaseValueObject[str]):
    def validate(self):
        return

    def as_generic_type(self) -> str:
        return str(self.value)
