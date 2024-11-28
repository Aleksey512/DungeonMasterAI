import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from gateway.application.api.lifespan import lifespan
from gateway.settings.logging import DEBUG, setup_logging

conf = {
    "app": "gateway.application.api.main:create_app",
    "host": "0.0.0.0",
    "port": 8000,
    "log_config": setup_logging(),
    "log_level": "debug" if DEBUG else "info",
    "reload": True,
}


def create_app() -> FastAPI:
    app = FastAPI(
        title="API Gateway",
        root_path="/api",
        lifespan=lifespan,
    )
    app.add_middleware(  # type: ignore[arg-type]
        CORSMiddleware,  # type: ignore
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


if __name__ == "__main__":
    uvicorn.run(**conf)
