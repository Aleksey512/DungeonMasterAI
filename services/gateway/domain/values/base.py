from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

VT = TypeVar("VT", bound=Any)


@dataclass(frozen=True)
class BaseValueObject(ABC, Generic[VT]):
    """Abstract base class for immutable Value Objects.

    A Value Object is defined by its attributes rather than an identity.
    This class provides a base implementation for creating custom value
    objects, enforcing immutability and validation rules.

    Attributes:
        value (VT): The encapsulated value of the object. The type is
            specified using the `Generic` type variable `VT`.

    Methods:
        validate():
            Abstract method that must be implemented to define validation
            logic for the encapsulated value.

        as_generic_type() -> VT:
            Abstract method that must return the value as its original
            generic type.

        __eq__(value: object) -> bool:
            Compares the value object with another object for equality
            based on the encapsulated value.
    """

    value: VT

    def __post_init__(self):
        """Called after the object is initialized.

        Ensures that the value is validated according to the logic
        defined in the `validate` method.
        """
        self.validate()

    @abstractmethod
    def validate(self):
        """Abstract method to validate the encapsulated value. This method must
        be implemented by subclasses to enforce specific rules.

        Raises:
            ValueError: If the encapsulated value does not meet validation criteria.
        """

    @abstractmethod
    def as_generic_type(self) -> VT:
        """Abstract method that must return the encapsulated value in its
        original type.

        Returns:
            VT: The encapsulated value as its original type.
        """

    def __eq__(self, value: object, /) -> bool:
        """Compares this Value Object with another object for equality based on
        the encapsulated value.

        Args:
            value (object): The object to compare with.

        Returns:
            bool: `True` if the encapsulated values are equal, `False` otherwise.
        """
        return self.as_generic_type() == value
