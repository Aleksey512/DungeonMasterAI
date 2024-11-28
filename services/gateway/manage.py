import sys
from pathlib import Path

import uvicorn
from alembic import command
from alembic.config import Config
from gateway.application.api.main import conf

ROOT_DIR = Path(__file__).resolve().parent
ALEMBIC_CONFIG = ROOT_DIR / "alembic.ini"
ALEMBIC_SCRIPT_LOCATION = ROOT_DIR / "migrations"


def runserver():
    """Запуск сервера через uvicorn API."""
    uvicorn.run(**conf)


def migrate():
    """Применение миграций через Alembic API."""
    config = Config(ALEMBIC_CONFIG)
    config.set_main_option("script_location", str(ALEMBIC_SCRIPT_LOCATION))
    command.upgrade(config, "head")


def makemigration(name: str):
    """Создание новой миграции через Alembic API."""
    config = Config(ALEMBIC_CONFIG)
    config.set_main_option("script_location", str(ALEMBIC_SCRIPT_LOCATION))
    command.revision(config, message=name, autogenerate=True)


def main():
    """Главная точка входа."""
    if len(sys.argv) < 2:
        print("Укажите команду: runserver, migrate, или makemigration <name>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "runserver":
        runserver()
    elif command == "migrate":
        migrate()
    elif command == "makemigration":
        if len(sys.argv) < 3:
            print(
                "Укажите имя для новой миграции."
                + "Например: makemigration add_users_table"
            )
            sys.exit(1)
        name = sys.argv[2]
        makemigration(name)
    else:
        print(
            f"Неизвестная команда: {command}. "
            + "Используйте runserver, migrate, или makemigration <name>"
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
