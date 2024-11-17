import re
from dataclasses import dataclass


@dataclass(eq=False)
class ApplicationError(Exception):
    """Base class for application-specific exceptions.

    This class provides a unified structure for defining exceptions with a
    consistent message and type format. The `type` property automatically
    generates a snake_case version of the class name prefixed with "sso_".

    Properties:
        message (str): A user-defined message describing the error.
            Default is "Base application exception".
        type (str): The type of the error in the format `sso_<snake_case_class_name>`.

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
            ...     print(e.type)     # Output: sso_invalid_credentials_error
    """

    @property
    def message(self) -> str:
        """Returns the error message.

        Override this property in subclasses to provide a custom error message.

        Returns:
            str: The default error message, "Base application exception".
        """
        return "Base application exception"

    @property
    def type(self) -> str:
        """Returns the error type in snake_case format prefixed with "sso_".

        The type is automatically derived from the class name using the
        `_to_snake_case` method.

        Returns:
            str: The type of the error, e.g., "sso_custom_error".
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
