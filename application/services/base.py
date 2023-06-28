import os

from abc import ABC, abstractmethod

class BaseService(ABC):

    @abstractmethod
    def protocol() -> str:
        raise NotImplementedError()
    
    @abstractmethod
    def host() -> str:
        raise NotImplementedError()

    @abstractmethod
    def port() -> int:
        raise NotImplementedError()

    @abstractmethod
    def url_env_var() -> str:
        raise NotImplementedError()

    @property
    def base_url(self) -> str:
        try:
            base_url: str = os.environ[self.url_env_var()]
        except KeyError:
            base_url: str = f"{self.protocol()}://{self.host()}:{self.port()}"
        
        return base_url