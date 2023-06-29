import requests

from application.services.base import BaseService


class BIService(BaseService):

    def protocol(self) -> str:
        return "https"
    
    def host(self) -> str:
        return "biservice.imd.ufrn.br"

    def port(self) -> int:
        return 80

    def url_env_var(self) -> str:
     return "BI_SERVICE_URL"

    def atualizarDashTwitter(self, ids: dict):
        
        url: str = f"{self.base_url}/atualizarDashTwitter"

        response: requests.Response = requests.get(url, json=ids)
        response.raise_for_status()

        return response.json()

