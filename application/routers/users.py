import requests

from typing import List
from typing import NoReturn

from fastapi import APIRouter
from fastapi import HTTPException

from application.services.account import AccountService
from application.models.users import User
from application.models.users import UserCreation
from application.models.users import DocumentType

tag: str = "Users"

description: str = """

"""

router = APIRouter(
    prefix="/users",
    tags=[tag],
)

@router.get(
    path="",
    response_model=List[User],
    status_code=200,
    summary="Retrieve all users",
    description="Retrieve a list containing all registered users.",
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

@router.post(
    path="",
    response_model=User,
    status_code=201,
    summary="Create user",
    description="Create an user by passing user information."
)
async def create_user(user_creation: UserCreation) -> User:
    try:
        user: User = AccountService().create_user(user_creation)
    except requests.HTTPError as error:
        raise HTTPException(error.response.status_code)

    return user

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
async def delete_user(id: str) -> NoReturn:
    try:
        AccountService().delete_user(id)
    except requests.HTTPError as error:
        raise HTTPException(error.response.status_code)