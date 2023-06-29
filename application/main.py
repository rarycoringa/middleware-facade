from typing import Dict

from fastapi import FastAPI

from application.routers.users import router as users_router
# from application.routers.apps import router as apps_router

app = FastAPI(
    title="Facade API",
    description=(
        "Facade API helps you to create and manage social publications 🌐"
        "<br/>Here ofaefaefefaea"
    ),
    version="1.0",
    openapi_tags=[
        {
            "name": users_router.tags[0],
            "description": "some desc."
        }
    ],
    docs_url="/swaggerdocs",
    redoc_url="/docs",
    contact={
        "name": "Rary Coringa",
        "email": "rary.goncalves.123@ufrn.edu.br",
    }
)

app.include_router(users_router)
# app.include_router(apps_router)