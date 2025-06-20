import re
from dataclasses import dataclass


@dataclass(eq=False, frozen=True)
class BaseError(Exception):
    """Base class for application-specific exceptions.

    This class provides a unified structure for defining exceptions with a
    consistent message and type format. The `type` property automatically
    generates a snake_case version of the class name.

    Properties:
        message (str): A user-defined message describing the error.
            Default is "Base application exception".
        ex_type (str): The type of the error in the format `<snake_case_class_name>`.

    Methods:
        _to_snake_case(cls): Converts the class name to snake_case format.

    Examples:
        Creating a custom error class:
            >>> class InvalidCredentialsError(ApplicationError):
            ...     @property
            ...     def message(self) -> str:
            ...         return "Invalid credentials provided"

        Raising and handling the custom error:
            >>> try:
            ...     raise InvalidCredentialsError()
            ... except ApplicationError as e:
            ...     print(e.message)  # Output: Invalid credentials provided
            ...     print(e.ex_type)     # Output: invalid_credentials_error
    """

    @property
    def message(self) -> str:
        """Returns the error message.

        Override this property in subclasses to provide a custom error message.

        Returns:
            str: The default error message, "Base application exception".
        """
        return "Base error"

    @property
    def ex_type(self) -> str:
        """Returns the error type in snake_case format.

        The type is automatically derived from the class name using the
        `_to_snake_case` method.

        Returns:
            str: The type of the error, e.g., "custom_error".
        """
        return self._to_snake_case()

    @classmethod
    def _to_snake_case(cls) -> str:
        """Converts the class name to snake_case format.

        For example, a class named `InvalidCredentialsError` will be converted
        to `invalid_credentials_error`.

        Returns:
            str: The class name in snake_case format.
        """
        name_with_underscores = re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__name__)
        return name_with_underscores.lower()
