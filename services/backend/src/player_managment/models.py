from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from src.core.infra.database.base import Base, PKMixin


class Player(Base, PKMixin):
    __tablename__ = "players"
    name: Mapped[str] = mapped_column(String(64))
    email: Mapped[str] = mapped_column(String(256), unique=True)
