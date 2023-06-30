import requests

from fastapi import APIRouter
from fastapi import HTTPException

from application.models.bi import IDs
from application.models.bi import Dashboard_data
from application.services.bi import BIService


bi_tag: str = "BI"

router = APIRouter(
    prefix = "/bi",
    tags = [bi_tag]
)

@router.get(
    path = "",
    reponse_model=Dashboard_data,
    status_code=200,
    summary="Refresh Twitter dashboard",
)

async def refresh_twitter_dashboard(ids: IDs) -> Dashboard_data:
    try:
        dashboard_data: Dashboard_data = BIService().refresh_twitter_dashboard(ids)
    except requests.HTTPError as error:
        raise HTTPException(error.response.status)
    
    return dashboard_data




