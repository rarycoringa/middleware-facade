import requests

from typing import List

from fastapi import APIRouter
from fastapi import HTTPException

from application.services.account import AccountService
from application.models.users import User
from application.models.users import UserCreation
from application.models.users import DocumentType

users_tag: str = "Users"

router = APIRouter(
    prefix="/users",
    tags=[users_tag],
)

@router.get(
    path="",
    response_model=List[User],
    status_code=200,
    summary="Retrieve all users",
    description="Retrieve a list containing all available users.",
)
async def retrieve_users() -> List[User]:
    try:
        users: List[User] = AccountService().retrieve_users()
    except requests.HTTPError as error:
        raise HTTPException(error.response.status_code)
    
    return users

@router.get(
    path="/{id}",
    response_model=User,
    status_code=200,
    summary="Retrieve user",
    description="Retrieve an user by passing user ID.",
)
async def retrieve_user(id: str) -> User:
    try:
        user: User = AccountService().retrieve_user(id)
    except requests.HTTPError as error:
        raise HTTPException(error.response.status_code)

    return user

@router.get(
    path="/bydocument",
    response_model=User,
    status_code=200,
    summary="Retrieve user by document",
    description=(
        "Retrieve an user by passing a document."
        " These document types below are available to be retrieved by:"
        "\n- CPF"
        "\n- CNPJ"
    )
)
async def retrieve_user_by_document(type: DocumentType, number: str) -> User:
    try:
        user: User = AccountService().retrieve_user_by_document(type, number)
    except requests.HTTPError as error:
        raise HTTPException(error.response.status_code)

    return user

# @router.get(
#     path="/{id}/apps",
# )
# async def retrieve_user_apps_by_id(id: str):
#     return AccountService().retrieve_user_apps_by_id(id)

@router.post(
    path="",
    response_model=User,
    status_code=201,
    summary="Create user",
    description="Create an user by passing user informations."
)
async def create_user(user_creation: UserCreation) -> User:
    try:
        user: User = AccountService().create_user(user_creation)
    except requests.HTTPError as error:
        raise HTTPException(error.response.status_code)

    return user

# @router.post(
#     path="/withapp",
# )
# async def create_user_with_app(userwithapp):
#     return AccountService().create_user_with_app(user.user, user.app)

@router.put(
    path="",
    response_model=User,
    status_code=201,
    summary="Update user",
    description="Update an user information by passing new values."
)
async def update_user(user: User) -> User:
    try:
        user: User = AccountService().update_user(user)
    except requests.HTTPError as error:
        raise HTTPException(error.response.status_code)

    return user

@router.delete(
    path="/{id}",
    response_model=None,
    status_code=204,
    summary="Delete user",
    description="Delete an user by passing user ID.",
)
async def delete_user(id: str) -> None:
    try:
        user: User = AccountService().delete_user(id)
    except requests.HTTPError as error:
        raise HTTPException(error.response.status_code)