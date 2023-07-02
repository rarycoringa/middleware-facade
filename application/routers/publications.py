import requests

from typing import List
from typing import NoReturn

from fastapi import APIRouter
from fastapi import HTTPException

from application.services.publications import PublicationService
from application.models.publications import Publication
from application.models.publications import PublicationCreation


tag: str = "Publications"

description: str = """

"""

router = APIRouter(
    prefix="/publications",
    tags=[tag],
)

@router.get(
    path="",
    response_model=List[Publication],
    status_code=200,
    summary="Retrieve all publications",
    description="Retrieve a list containing all publications.",
)
async def retrieve_publications() -> List[Publication]:
    try:
        pubs: List[Publication] = PublicationService().retrieve_publications()
    except requests.HTTPError as error:
        raise HTTPException(error.response.status_code)
    
    return pubs

@router.get(
    path="/{id}",
    response_model=Publication,
    status_code=200,
    summary="Retrieve publication",
    description="Retrieve a publication by passing the publication ID.",
)
async def retrieve_publication(id: int) -> Publication:
    try:
        publication: Publication = PublicationService().retrieve_publication(id)
    except requests.HTTPError as error:
        raise HTTPException(error.response.status_code)

    return publication

@router.get(
    path="/user/{user_id}",
    response_model=Publication,
    status_code=200,
    summary="Retrieve user publications",
    description="Retrieve all publications of an user by passing the user ID.",
)
async def retrieve_publications_by_user(user_id: str) -> List[Publication]:
    try:
        publications: Publication = PublicationService().retrieve_publications_by_user(user_id)
    except requests.HTTPError as error:
        raise HTTPException(error.response.status_code)

    return publications

@router.post(
    path="",
    response_model=Publication,
    status_code=201,
    summary="Create publication",
    description="Create a publication by passing the publication information."
)
async def create_publication(publication_creation: PublicationCreation) -> Publication:
    try:
        pub_create: Publication = PublicationService().create_publication(publication_creation)
    except requests.HTTPError as error:
        raise HTTPException(error.response.status_code)

    return pub_create


@router.put(
    path="",
    response_model=Publication,
    status_code=201,
    summary="Update publication",
    description="Update a publication by passing the new publication information."
)
async def update_pub(publication: Publication) -> Publication:
    try:
        publication: Publication = PublicationService().update_publication(publication)
    except requests.HTTPError as error:
        raise HTTPException(error.response.status_code)

    return publication

@router.delete(
    path="{id}",
    response_model=None,
    status_code=204,
    summary="Delete publication",
    description="Delete a publication by passing the publication ID.",
)
async def delete_publication(id: int) -> NoReturn:
    try:
        PublicationService().delete_publication(id)
    except requests.HTTPError as error:
        raise HTTPException(error.response.status_code)
