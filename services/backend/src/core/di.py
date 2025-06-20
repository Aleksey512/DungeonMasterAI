from functools import lru_cache

import punq

from src.player_managment.repository import PlayerRepository
from src.player_managment.service import PlayerManagmentService


@lru_cache(1)
def init_container() -> punq.Container:
    return _init_container()


def _init_repositories(container: punq.Container) -> None:
    container.register(
        PlayerRepository, factory=lambda: PlayerRepository(), scope=punq.Scope.transient
    )


def _init_svc(container: punq.Container) -> None:
    container.register(PlayerManagmentService, scope=punq.Scope.transient)


def _init_container() -> punq.Container:
    container = punq.Container()
    _init_repositories(container)
    _init_svc(container)
    return container
