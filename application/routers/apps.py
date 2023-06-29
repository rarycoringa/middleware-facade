from fastapi import APIRouter

apps_tag: str = "Apps"

router = APIRouter(
    prefix="/apps",
    tags=[apps_tag]
)

