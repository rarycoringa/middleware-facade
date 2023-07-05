import requests

from application.services.base import BaseService
from application.models.bi import TwitterIDs
from application.models.bi import TwitterGraphics

class BIService(BaseService):

    def protocol(self) -> str:
        return "https"
    
    def host(self) -> str:
        return "biservice.imd.ufrn.br"

    def port(self) -> int:
        return 80

    def url_env_var(self) -> str:
     return "BI_SERVICE_URL"

    def retrieve_twitter_graphics(self, twitter_ids: TwitterIDs, mocked: bool = False) -> TwitterGraphics:
        if mocked:
            url: str = f"{self.base_url}/atualizarDashTwitterMockup"
        else:
            url: str = f"{self.base_url}/atualizarDashTwitter"

        response: requests.Response = requests.get(url, json=twitter_ids.to_service_format())
        response.raise_for_status()

        twitter_graphics: TwitterGraphics = TwitterGraphics.from_service_format(response.json())

        return twitter_graphics
