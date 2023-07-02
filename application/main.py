from typing import Dict

from fastapi import FastAPI
from application.routers.bi import router as bi_router

app = FastAPI()

@app.get("/")
async def main():
    response: Dict[str, str] = {"name": "Facade", "version": "v1.0"}

    return response

app.include_router(bi_router)