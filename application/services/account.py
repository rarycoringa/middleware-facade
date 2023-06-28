import requests

from enum import Enum

from application.services.base import BaseService

class UserRetrievalTypeEnum(Enum):
    ID: str = "ID"
    CPF: str = "CPF"
    CNPJ: str = "CNPJ"

class AccountService(BaseService):

    def protocol(self) -> str:
        return "https"
    
    def host(self) -> str:
        return "accountservice.imd.ufrn.br"

    def port(self) -> int:
        return 80
    
    def url_env_var(self) -> str:
        return "ACCOUNT_SERVICE_URL"

    def retrieve_users(self):
        url: str = f"{self.base_url}/users"

        response: requests.Response = requests.get(url)
        response.raise_for_status()

        return response.json()

    def _retrieve_user(self, value: str, type: UserRetrievalTypeEnum):
        match type:
            case UserRetrievalTypeEnum.ID:
                url: str = f"{self.base_url}/users/{value}"
            case UserRetrievalTypeEnum.CPF:
                url: str = f"{self.base_url}/users/cpf/{value}"
            case UserRetrievalTypeEnum.CNPJ:
                url: str = f"{self.base_url}/users/cnpj/{value}"
        
        response: requests.Response = requests.get(url)
        response.raise_for_status()

        return response.json()

    def retrieve_user_by_id(self, id: str):
        type: UserRetrievalTypeEnum = UserRetrievalTypeEnum.ID

        return self._retrieve_user(value=id, type=type)

    def retrieve_user_by_cpf(self, cpf: str):
        type: UserRetrievalTypeEnum = UserRetrievalTypeEnum.CPF

        return self._retrieve_user(value=cpf, type=type)

    def retrieve_user_by_cnpj(self, cnpj: str):
        type: UserRetrievalTypeEnum = UserRetrievalTypeEnum.CNPJ

        return self._retrieve_user(value=cnpj, type=type)

    def retrieve_user_apps_by_id(self, id: str):
        url = f"{self.base_url}/users/{id}/apps"

        response = requests.get(url)
        response.raise_for_status()

        return response.json()

    def create_user(self, user: dict):
        url = f"{self.base_url}/users"

        response = requests.post(url, json=user)
        response.raise_for_status()

        return response.json()

    def create_user_with_app(self, user: dict, app: dict):
        url = f"{self.base_url}/users/with-app"

        user_with_app = {
            "user": user,
            "app": app,
        }

        response = requests.post(url, json=user_with_app)
        response.raise_for_status()

        return response.json()

    def update_user(self, user: dict):
        url = f"{self.base_url}/users"

        response = requests.put(url, json=user)
        response.raise_for_status()

        return response.json()

    def delete_user(self):
        url = f"{self.base_url}/users/{id}"

        response = requests.delete(url)
        response.raise_for_status()

        return response.json()

    def retrieve_apps_by_user_id(self, id: str):
        url = f"{self.base_url}/apps/{id}"

        response = requests.get(url)
        response.raise_for_status()

        return response.json()

    def create_app(self, app: dict):
        url = f"{self.base_url}/apps"

        response = requests.post(url, json=app)
        response.raise_for_status()

        return response.json()

    def update_app(self, app: dict):
        url = f"{self.base_url}/apps"

        response = requests.put(url, json=app)
        response.raise_for_status()

        return response.json()

    def delete_app(self, id: str):
        url = f"{self.base_url}/apps/{id}"

        response = requests.delete(url)
        response.raise_for_status()

        return response.json()