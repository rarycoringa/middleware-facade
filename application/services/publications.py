import requests

from typing import List
from typing import NoReturn

from application.services.base import BaseService
from application.models.publications import Publication
from application.models.publications import PublicationCreation

class PublicationService(BaseService):

    def protocol(self) -> str:
        return "https"
    
    def host(self) -> str:
        return "publicationservice.imd.ufrn.br"

    def port(self) -> int:
        return 80

    def url_env_var(self) -> str:
        return "PUBLICATION_SERVICE_URL"

    def retrieve_publications(self) -> List[Publication]:
        url: str = f"{self.base_url}/pubs"

        response: requests.Response = requests.get(url)
        response.raise_for_status()

        publications: List[Publication] = [
            Publication.from_service_format(publication)
            for publication in response.json()
        ]

        return publications
    
    def retrieve_publication(self, id: int) -> Publication:
        url: str = f"{self.base_url}/pubs/{id}"

        response: requests.Response = requests.get(url)
        response.raise_for_status()

        publication: Publication = Publication.from_service_format(response.json())

        return publication
    
    def retrieve_publications_by_user(self, user_id: str) -> List[Publication]:
        url: str = f"{self.base_url}/pubs/user/{user_id}"

        response: requests.Response = requests.get(url)
        response.raise_for_status()

        publications: List[Publication] = [
            Publication.from_service_format(publication)
            for publication in response.json()
        ]

        return publications


    def create_publication(self, publication_creation: PublicationCreation) -> Publication:
        url: str = f"{self.base_url}/pubs"

        response: requests.Response = requests.post(url, json=publication_creation.to_service_format())
        response.raise_for_status()

        publication: Publication = Publication.from_service_format(response.json())

        return publication

    def update_publication(self, publication: Publication) -> Publication:
        url: str = f"{self.base_url}/pubs"

        response: requests.Response = requests.put(url, json=publication.to_service_format())
        response.raise_for_status()

        publication: Publication = Publication.from_service_format(response.json())

        return publication

    def delete_publication(self, id: int) -> NoReturn:
        url: str = f"{self.base_url}/pubs/{id}"

        response: requests.Response = requests.delete(url)
        response.raise_for_status()
