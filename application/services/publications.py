import requests

from typing import List

from application.services.base import BaseService
from application.models.publications import Publication


class PublicationService(BaseService):

    def protocol(self) -> str:
        return "https"
    
    def host(self) -> str:
        return "publicationservice.imd.ufrn.br"

    def port(self) -> int:
        return 80

    def url_env_var(self) -> str:
        return "PUBLICATION_SERVICE_URL"


#Para todas as publicações
    def retrieve_pubs(self ) -> List[Publication]:
        url: str = f"{self.base_url}/pubs"

        response: requests.Response = requests.get(url)
        response.raise_for_status()

        pubs: List[Publication] = [
            Publication.formater_of_response(publication)
            for publication in response.json()
        ]

        return pubs
    

#Para determinada publicação pelo ID da publicação
    def retrieve_pub(self, pub_id: int) -> Publication:
        url = f"{self.base_url}/pubs/{pub_id}"

        response = requests.Response = requests.get(url)
        response.raise_for_status()

        pub: Publication = Publication.formater_of_response(response.json())

        return pub
    

#Para retornar todas as publicações de um mesmo usuário
    def retrieve_pubs_by_user(self, user: str) -> List[Publication]:
        url = f"{self.base_url}/pubs/user/{user}"

        response: requests.Response = requests.get(url)
        response.raise_for_status()

        pubs_user: List[Publication] = [
            Publication.formater_of_response(publication)
            for publication in response.json()
        ]

        return pubs_user


#Para salvar uma publicação
    def create_pub(self, pub: Publication):
        url = f"{self.base_url}/pubs"

        response = requests.post(url, json=pub.formater_of_response())
        response.raise_for_status()

        pub_create: Publication = Publication.formater_of_response(response.json())

        return pub_create


#Para atualizar uma publicação
    def update_pub(self, pub: dict):
        url = f"{self.base_url}/pubs"

        response = requests.put(url, json=pub)
        response.raise_for_status()

        return response.json()


#Para deletar uma publicação pelo ID da publicação
    def delete_pub_by_pub_id(self, pub_id: int) -> None:
        url = f"{self.base_url}/pubs/{pub_id}"

        response = requests.delete(url)
        response.raise_for_status()
