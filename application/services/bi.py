from application.services.base import BaseService

class BIService(BaseService):

    def protocol(self) -> str:
        return "https"
    
    def host(self) -> str:
        return "biservice.imd.ufrn.br"

    def port(self) -> int:
        return 80
