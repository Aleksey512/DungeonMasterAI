"""
FastApi integrations di
"""

from typing import Any

from fastapi import Depends
from src.core.di import init_container


def resolve_dependency(cls: Any) -> Any:
    """
    Usage:

    @router.post("/")
    async def create(svc: GameSessionService = resolve_dependency(GameSessionService)):
    """

    async def _resolve() -> Any:
        return init_container().resolve(cls)

    return Depends(_resolve)
