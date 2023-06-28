from enum import Enum

import requests

from application.services.base import BaseService


class UserRetrievalTypeEnum(Enum):
    PUB_ID: int = "PUB_ID"
    USER: str = "USER"

class PublicationService(BaseService):

    def protocol(self) -> str:
        return "https"
    
    def host(self) -> str:
        return "publicationservice.imd.ufrn.br"

    def port(self) -> int:
        return 80

    def url_env_var(self) -> str:
        return "PUBLICATION_SERVICE_URL"

    def retrieve_pubs(self ):
        url: str = f"{self.base_url}/pubs"

        response: requests.Response = requests.get(url)
        response.raise_for_status()

        return response.json()
    
    def retrieve_user_pubs_by_pub_id(self, pub_id: str):
        url = f"{self.base_url}/pubs/{pub_id}"

        response = requests.get(url)
        response.raise_for_status()

        return response.json()
    
    def retrieve_pubs_by_user(self, user: str):
        url = f"{self.base_url}/pubs/user/{user}"

        response = requests.get(url)
        response.raise_for_status()

        return response.json()

    def create_pubs(self, user: dict):
        url = f"{self.base_url}/pubs"

        response = requests.post(url, json=user)
        response.raise_for_status()

        return response.json()

    def update_pubs(self, user: dict):
        url = f"{self.base_url}/pubs"

        response = requests.put(url, json=user)
        response.raise_for_status()

        return response.json()

    def delete_pubs_by_pub_id(self, pub_id: str):
        url = f"{self.base_url}/pubs/{pub_id}"

        response = requests.delete(url)
        response.raise_for_status()

        return response.json()