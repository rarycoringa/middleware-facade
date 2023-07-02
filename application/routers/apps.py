import requests

from typing import List
from typing import NoReturn

from fastapi import APIRouter
from fastapi import HTTPException

from application.services.accounts import AccountService
from application.models.apps import App
from application.models.apps import AppCreation

tag: str = "Apps"

description: str = """

"""

router = APIRouter(
    prefix="/apps",
    tags=[tag],
)

@router.get(
    path="/{user_id}",
    response_model=List[App],
    status_code=200,
    summary="Retrieve user apps",
    description="Retrieve a list containing all registered apps from an user.",
)
async def retrieve_apps_by_user_id(user_id: str) -> List[App]:
    try:
        apps: List[App] = AccountService().retrieve_apps_by_user_id(user_id)
    except requests.HTTPError as error:
        raise HTTPException(error.response.status_code)
    
    return apps

@router.post(
    path="",
    response_model=App,
    status_code=201,
    summary="Create app",
    description="Create an app by passing app information.",
)
async def create_app(app_creation: AppCreation) -> App:
    try:
        app: App = AccountService().create_app(app_creation)
    except requests.HTTPError as error:
        raise HTTPException(error.response.status_code)

    return app

@router.put(
    path="",
    response_model=App,
    status_code=201,
    summary="Update app",
    description="Update an app information by passing new values.",
)
async def update_app(app: App) -> App:
    try:
        app: App = AccountService().update_app(app)
    except requests.HTTPError as error:
        raise HTTPException(error.response.status_code)

    return app

@router.delete(
    path="/{user_id}",
    response_model=None,
    status_code=204,
    summary="Delete app",
    description="Delete an app by passing the owner user ID.",
)
async def delete_app(user_id: str) -> NoReturn:
    try:
        AccountService().delete_app(user_id)
    except requests.HTTPError as error:
        raise HTTPException(error.response.status_code)
