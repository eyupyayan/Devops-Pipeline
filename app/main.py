import logging
from fastapi import FastAPI

from .config import get_settings
from .routes import router

def create_app() -> FastAPI:
    settings = get_settings()
    logging.basicConfig(level=settings["LOG_LEVEL"].upper())
    app = FastAPI(title=settings["APP_NAME"])
    app.include_router(router)
    return app

app = create_app()