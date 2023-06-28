from typing import Dict

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main():
    response: Dict[str, str] = {"name": "Facade", "version": "v1.0"}

    return response