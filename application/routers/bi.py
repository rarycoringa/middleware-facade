import requests

from fastapi import APIRouter
from fastapi import HTTPException

from application.models.bi import IDs
from application.models.bi import TwitterDashboardData
from application.services.bi import BIService


bi_tag: str = "BI"

router = APIRouter(
    prefix = "/bi",
    tags = [bi_tag]
)

@router.get(
    path = "",
    reponse_model=TwitterDashboardData,
    status_code=200,
    summary="Refresh Twitter dashboard",
)

async def refresh_twitter_dashboard(ids: IDs) -> TwitterDashboardData:
    try:
        twitter_dashboard_data: TwitterDashboardData = BIService().refresh_twitter_dashboard(ids)
    except requests.HTTPError as error:
        raise HTTPException(error.response.status)
    
    return twitter_dashboard_data




