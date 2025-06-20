from uuid import UUID, uuid4

from sqlalchemy import UUID as SQL_UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase): ...


class PKMixin:
    id: Mapped[UUID] = mapped_column(
        SQL_UUID(), default=uuid4, primary_key=True
    )
