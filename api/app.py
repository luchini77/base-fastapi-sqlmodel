from fastapi import FastAPI

from api.database import create_tables
from api.public import api as public_api


def create_app():
    app = FastAPI(
        title="Tareas Kukianas",
        version="0.1"
    )

    @app.on_event("startup")
    def on_starup():
        create_tables()


    app.include_router(public_api)

    return app