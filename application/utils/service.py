from abc import ABC, abstractmethod
from typing import Tuple

class ServiceInterface(ABC):
    @abstractmethod
    def host(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def port(self) -> int:
        raise NotImplementedError()

    @abstractmethod
    def get_auth(self) -> Tuple[str, str]:
        raise NotImplementedError()

    @abstractmethod
    def protocol(self) -> str:
        raise NotImplementedError()

    def base_url(self) -> str:
        return f"{self.protocol()}://{self.host()}:{self.port()}"