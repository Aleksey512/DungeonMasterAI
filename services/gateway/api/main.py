import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from gateway.api.lifespan import lifespan
from gateway.settings.logging import DEBUG, setup_logging


def create_app() -> FastAPI:
    app = FastAPI(
        title="AllocUp SSO",
        root_path="/api",
        lifespan=lifespan,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


def main():
    conf = {
        "app": "api.main:create_app",
        "host": "0.0.0.0",
        "port": 8000,
        "log_config": setup_logging(),
        "log_level": "debug" if DEBUG else "info",
        "reload": True,
    }
    uvicorn.run(**conf)


if __name__ == "__main__":
    main()
