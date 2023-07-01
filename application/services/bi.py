import requests

from application.services.base import BaseService
from application.models.bi import IDs
from application.models.bi import TwitterDashboardData

class BIService(BaseService):

    def protocol(self) -> str:
        return "https"
    
    def host(self) -> str:
        return "biservice.imd.ufrn.br"

    def port(self) -> int:
        return 80

    def url_env_var(self) -> str:
     return "BI_SERVICE_URL"

    def retrieve_twitter_dashboard_data(self, ids: IDs) -> TwitterDashboardData:
        
        url: str = f"{self.base_url}/atualizarDashTwitter"

        response: requests.Response = requests.get(url, json=ids.formater_of_request())
        response.raise_for_status()

        twitter_dashboard_data: TwitterDashboardData = TwitterDashboardData.formater_of_response(response.json())

        return twitter_dashboard_data
