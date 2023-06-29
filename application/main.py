from fastapi import FastAPI

# from application.routers.apps import router as apps_router
# from application.routers.bi import router as bi_router
# from application.routers.publications import router as publications_router
from application.routers.users import router as users_router

description: str = """
Facade API helps you to manage your **Social Media Content** 🌐

Here you will be able to enjoy all available resources on the **Social Media Middleware**, as you can see below:
1. You can manage publications in a lot of social media plataforms at the same time.
2. You can retrieve BI analytics about your publications and your social media accounts.
"""

app = FastAPI(
    title="Facade API",
    description=description,
    version="1.0",
    openapi_tags=[
        # {"name": apps_router.tags[0], "description": "some desc."},
        # {"name": bi_router.tags[0], "description": "some desc."},
        # {"name": publications_router.tags[0], "description": "some desc."},
        {"name": users_router.tags[0], "description": "some desc."},
    ],
    docs_url="/swaggerdocs",
    redoc_url="/docs",
    contact={
        "name": "Rary Coringa",
        "email": "rary.goncalves.123@ufrn.edu.br",
    }
)

# app.include_router(apps_router)
# app.include_routers(bi_router)
# app.include_routers(publications_router)
app.include_router(users_router)