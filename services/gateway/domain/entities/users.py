import hashlib
import hmac
from dataclasses import dataclass

from gateway.domain.entities.base import BaseEntity
from gateway.domain.events.users import UserCreatedEvent
from gateway.domain.values.users import CleanPassword, Email, HashablePassword
from gateway.settings.config import Config


@dataclass(eq=False)
class User(BaseEntity):
    email: Email
    hashed_password: HashablePassword

    @staticmethod
    def hash_password(password: str) -> str:
        password_bytes = password.encode("utf-8")
        secret_key_bytes = Config().secret_key.encode("utf-8")  # type:ignore

        hmac_hash = hmac.new(secret_key_bytes, password_bytes, hashlib.sha256)

        hashed_password = hmac_hash.hexdigest()

        return hashed_password

    @classmethod
    def create(cls, email: Email, password: CleanPassword) -> "User":
        hashed_password = cls.hash_password(password.as_generic_type())

        user = cls(email=email, hashed_password=HashablePassword(hashed_password))
        user.register_event(UserCreatedEvent(email=email.as_generic_type()))

        return user

    def check_password(self, password: str) -> bool:
        hashed_password = self.hash_password(password)
        return hashed_password == self.hashed_password

    def set_password(self, new_pass: CleanPassword):
        hashed_password = self.hash_password(new_pass.as_generic_type())
        self.hashed_password = HashablePassword(hashed_password)

    def to_dict(self) -> dict:
        return {
            "oid": self.oid,
            "created_at": self.created_at,
            "email": self.email.as_generic_type(),
        }
