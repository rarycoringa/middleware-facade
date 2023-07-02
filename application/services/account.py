import requests

from typing import List
from typing import NoReturn

from application.services.base import BaseService
from application.models.users import User
from application.models.users import UserCreation
from application.models.users import Document
from application.models.apps import App
from application.models.apps import AppCreation

class AccountService(BaseService):

    def protocol(self) -> str:
        return "https"
    
    def host(self) -> str:
        return "accountservice.imd.ufrn.br"

    def port(self) -> int:
        return 80
    
    def url_env_var(self) -> str:
        return "ACCOUNT_SERVICE_URL"

    def retrieve_users(self) -> List[User]:
        url: str = f"{self.base_url}/users"

        response: requests.Response = requests.get(url)
        response.raise_for_status()

        users: List[User] = [
            User.from_service_format(user)
            for user in response.json()
        ]

        return users

    def retrieve_user(self, id: str) -> User:
        url: str = f"{self.base_url}/users/{id}"

        response: requests.Response = requests.get(url)
        response.raise_for_status()

        user: User = User.from_service_format(response.json())

        return user

    def retrieve_user_by_document(self, document: Document) -> User:
        url: str = f"{self.base_url}/users/{document.type.value.lower()}/{document.number}"

        response: requests.Response = requests.get(url)
        response.raise_for_status()

        user: User = User.from_service_format(response.json())

        return user

    # def retrieve_user_apps_by_id(self, id: str):
    #     url = f"{self.base_url}/users/{id}/apps"

    #     response = requests.get(url)
    #     response.raise_for_status()

    #     return response.json()

    def create_user(self, user_creation: UserCreation) -> User:
        url = f"{self.base_url}/users"

        response = requests.post(url, json=user_creation.to_service_format())
        response.raise_for_status()

        user: User = User.from_service_format(response.json())

        return user

    # def create_user_with_app(self, user: dict, app: dict):
    #     url = f"{self.base_url}/users/with-app"

    #     user_with_app = {
    #         "user": user,
    #         "app": app,
    #     }

    #     response = requests.post(url, json=user_with_app)
    #     response.raise_for_status()

    #     return response.json()

    def update_user(self, user: User) -> User:
        url = f"{self.base_url}/users"

        response = requests.put(url, json=user.to_service_format())
        response.raise_for_status()

        user: User = User.from_service_format(response.json())

        return user

    def delete_user(self, id: str) -> NoReturn:
        url = f"{self.base_url}/users/{id}"

        response = requests.delete(url)
        response.raise_for_status()

    def retrieve_apps_by_user_id(self, user_id: str) -> List[App]:
        url = f"{self.base_url}/apps/{user_id}"

        response = requests.get(url)
        response.raise_for_status()

        apps: List[App] = [
            App.from_service_format(app)
            for app in response.json()
        ]

        return apps

    def create_app(self, app_creation: AppCreation) -> App:
        url = f"{self.base_url}/apps"

        response = requests.post(url, json=app_creation.to_service_format())
        response.raise_for_status()

        app: App = App.from_service_format(response.json())

        return app

    def update_app(self, app: App) -> App:
        url = f"{self.base_url}/apps/{app.id}"

        response = requests.put(url, json=app.to_service_format())
        response.raise_for_status()

        app: App = App.from_service_format(response.json())

        return app

    def delete_app(self, id: str) -> NoReturn:
        url = f"{self.base_url}/apps/{id}"

        response = requests.delete(url)
        response.raise_for_status()