import requests

from fastapi import APIRouter
from fastapi import HTTPException

from application.models.bi import TwitterIDs
from application.models.bi import TwitterGraphics
from application.services.bi import BIService

tag: str = "BI"

description: str = """

"""

router = APIRouter(
    prefix = "/bi",
    tags = [tag],
)

@router.get(
    path="/twitter",
    response_model=TwitterGraphics,
    status_code=200,
    summary="Retrieve Twitter graphics",
    description="Retrieve ",
)
async def retrieve_twitter_graphics(twitter_ids: TwitterIDs) -> TwitterGraphics:
    try:
        twitter_graphics: TwitterGraphics = BIService().retrieve_twitter_graphics(twitter_ids)
    except requests.HTTPError as error:
        raise HTTPException(error.response.status)
    
    return twitter_graphics




