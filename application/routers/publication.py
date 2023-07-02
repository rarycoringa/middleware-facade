import requests

from typing import List

from fastapi import APIRouter
from fastapi import HTTPException

from application.services.publication import PublicationService
from application.models.publication import Publication


pubs_tag: str = "Pubs"

router = APIRouter(
    prefix="/pubs",
    tags=[pubs_tag],
)


#Coletar todas as publicações
@router.get(
    path="",
    response_model=List[Publication],
    status_code=200,
    summary="Retrieve all publications",
    description="Retrieve a list containing all publications.",
)
async def retrieve_pubs() -> List[Publication]:
    try:
        pubs: List[Publication] = PublicationService().retrieve_pubs()
    except requests.HTTPError as error:
        raise HTTPException(error.response.status_code)
    
    return pubs


#Coletar uma publicação específica pelo ID da publicação
@router.get(
    path="/{pub_id}",
    response_model=Publication,
    status_code=200,
    summary="Retrieve a publication",
    description="Retrieve a publication by passing the publication ID.",
)
async def retrieve_pub(pub_id: int) -> Publication:
    try:
        pub: Publication = PublicationService().retrieve_pub(pub_id)
    except requests.HTTPError as error:
        raise HTTPException(error.response.status_code)

    return pub


#Para retornar todas as publicações de um mesmo usuário
@router.get(
    path="user/{user}",
    response_model=Publication,
    status_code=200,
    summary="Retrieve publications of a user",
    description="Retrieve all publications of a user passing the username.",
)
async def retrieve_pub(user: str) -> Publication:
    try:
        pub_user: Publication = PublicationService().retrieve_pubs_by_user(user)
    except requests.HTTPError as error:
        raise HTTPException(error.response.status_code)

    return pub_user


#Para salvar uma publicação
@router.post(
    path="",
    response_model=Publication,
    status_code=201,
    summary="Create a publication",
    description="Create a publication by passing the informations of the publication."
)
async def create_publication(pub: Publication) -> Publication:
    try:
        pub_create: Publication = PublicationService().create_pub(pub)
    except requests.HTTPError as error:
        raise HTTPException(error.response.status_code)

    return pub_create


#Para atualizar uma publicação
@router.put(
    path="",
    response_model=Publication,
    status_code=201,
    summary="Update a publication",
    description="Update a publication by passing the new information of the publication."
)
async def update_pub(pub: Publication) -> Publication:
    try:
        pub_update: Publication = PublicationService().update_pub(pub)
    except requests.HTTPError as error:
        raise HTTPException(error.response.status_code)

    return pub_update


#Para deletar uma publicação pelo ID da publicação
@router.delete(
    path="pubs/{pub_id}",
    response_model=None,
    status_code=204,
    summary="Delete a publication",
    description="Delete a publication by passing publication ID.",
)
async def delete_pub(pub_id: int) -> None:
    try:
        pub_delete: Publication = PublicationService().delete_pub_by_pub_id(pub_id)
    except requests.HTTPError as error:
        raise HTTPException(error.response.status_code)
