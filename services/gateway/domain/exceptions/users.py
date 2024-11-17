from dataclasses import dataclass

from gateway.domain.exceptions.base import ApplicationError


@dataclass(eq=False)
class InvalidEmailError(ApplicationError):
    email: str

    @property
    def message(self):
        email = self.email
        return f"Invalid email provided email={email}"


@dataclass(eq=False)
class InvalidPasswordError(ApplicationError):
    password: str

    @property
    def message(self):
        return "Invalid password provided"
