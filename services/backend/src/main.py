from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from src.core.exceptions.base import BaseError
from src.lifespan import lifespan
from src.player_managment.router import router as player_managment_router

app = FastAPI(title="DungeonMasterAI Backend", lifespan=lifespan)
app.include_router(player_managment_router)


@app.exception_handler(BaseError)
async def application_exception_handler(
    request: Request, exc: BaseError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"error": exc.message, "type": exc.ex_type},
    )


@app.get("/healthz")
async def healthz() -> str:
    return "ok"


@app.get("/readiness")
async def readiness() -> str:
    return "ready"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
        log_level="debug",
        workers=1,
    )
