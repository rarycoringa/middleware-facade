from fastapi import FastAPI

from application.routers.users import router as users_router
from application.routers.users import tag as users_tag
from application.routers.users import description as users_description
from application.routers.apps import router as apps_router
from application.routers.apps import tag as apps_tag
from application.routers.apps import description as apps_description

description: str = """
**Facade API helps you to manage your social media publications** 🌐

---

Here you will be able to know how to use and enjoy all available resources on the
**Social Media Middleware**, as you can see below:

- You can manage publications in a lot of social media platforms at the same time.
- You can retrieve BI analytics about your publications and your social media accounts.

---

Contributors:
- [Rary Coringa](https://github.com/rarycoringa)
- [Wendy Miller](https://github.com/leightonisrael)
- [Israel Hall](https://github.com/wendymillerr)

"""

app = FastAPI(
    title="Middleware Facade API",
    description=description,
    version="v1",
    openapi_tags=[
        {"name": users_tag, "description": users_description},
        {"name": apps_tag, "description": apps_description},
    ],
    docs_url="/swaggerdocs",
    redoc_url="/docs",
)

app.include_router(users_router)
app.include_router(apps_router)