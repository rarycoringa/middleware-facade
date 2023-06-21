import os

from abc import ABC, abstractmethod
from typing import Tuple

class ServiceInterface(ABC):
    @abstractmethod
    def protocol() -> str:
        raise NotImplementedError()
    
    @abstractmethod
    def host() -> str:
        raise NotImplementedError()

    @abstractmethod
    def port() -> int:
        raise NotImplementedError()

    def base_url(self) -> str:
        try:
            base_url: str = os.environ["ACCOUNT_SERVICE_URL"]
        except KeyError:
            base_url: str = f"{self.protocol()}://{self.host()}:{self.port()}"
        
        return base_url