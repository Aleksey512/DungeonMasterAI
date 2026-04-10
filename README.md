# DungeonMasterAI

An AI-powered Dungeons & Dragons application with microservices architecture. Features an AI DungeonMaster for story generation, game management, and multimedia content creation.

## Architecture

The project follows **Clean Architecture** with **CQRS** (Command Query Responsibility Segregation) and **Mediator** pattern.

```
┌──────────────────────────────────────────────────┐
│                  Application Layer                │
│              (FastAPI REST endpoints)             │
├──────────────────────────────────────────────────┤
│                   Logic Layer                     │
│         (Commands, Queries, Events, DI)           │
├──────────────────────────────────────────────────┤
│                  Domain Layer                     │
│       (Entities, Value Objects, Events)           │
├──────────────────────────────────────────────────┤
│               Infrastructure Layer                │
│     (SQLAlchemy, Repositories, Unit of Work)      │
└──────────────────────────────────────────────────┘
```

## Features

- **AI DungeonMaster** — story generation and game session management
- **Microservices** — independent services communicating via events
- **CQRS + Mediator** — custom mediator library for command/query/event separation
- **Domain-Driven Design** — aggregate roots, value objects, domain events
- **Unit of Work** — transactional consistency with async context managers

## Tech Stack

| Layer | Technology |
|-------|-----------|
| API | FastAPI, Uvicorn |
| ORM | SQLAlchemy 2.0 (async) |
| Migrations | Alembic |
| DI Container | punq |
| Auth | HMAC-SHA256, JWT (access + refresh tokens) |
| Build | Pants Build System |
| Containers | Docker |
| Linting | Black, isort, flake8, mypy |
| Testing | pytest, pytest-asyncio, Faker |

## Project Structure

```
├── libs/
│   └── python/
│       └── mediators/              # Custom CQRS mediator library
│           ├── handlers/           # Command, Query, Event handlers
│           ├── mediators/          # Mediator implementations
│           └── registries/         # Handler registries
├── services/
│   └── gateway/                    # Main API service
│       ├── application/api/        # FastAPI app and endpoints
│       ├── domain/                 # Entities, Value Objects, Events
│       ├── infra/                  # Repositories, Unit of Work
│       ├── logic/                  # DI container, mediator setup
│       ├── migrations/             # Alembic database migrations
│       ├── settings/               # Pydantic configuration
│       └── tests/                  # Unit and integration tests
└── docker/                         # Dockerfiles
```

## Getting Started

### Prerequisites

- Python 3.12+
- [Pants](https://www.pantsbuild.org/) build system
- Docker (optional)

### Development

```bash
# Install Pants
./get-pants.sh

# Run the gateway service
pants run services/gateway:main

# Run tests
pants test services/gateway/tests::

# Lint
pants lint ::

# Type check
pants check ::
```

### Docker

```bash
# Build and run
pants package services/gateway:docker
docker-compose up
```

## Mediator Library

The project includes a custom mediator library (`libs/python/mediators/`) implementing the CQRS pattern:

```python
# Register a command handler
@command_registry.register(CreateUserCommand)
class CreateUserHandler(CommandHandler):
    async def handle(self, command: CreateUserCommand) -> None:
        ...

# Dispatch through mediator
await mediator.handle_command(CreateUserCommand(email="user@example.com"))
```

## Authors

- [Aleksey512](https://github.com/Aleksey512)
- [JellyWilliam](https://github.com/JellyWilliam)

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
