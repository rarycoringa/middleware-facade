import requests

from typing import List
from typing import Optional

from fastapi import APIRouter
from fastapi import HTTPException

from application.services.account import AccountService
from application.models.users import User

apps_tag: str = "Apps"

router = APIRouter(
    prefix="/apps",
    tags=[apps_tag]
)

