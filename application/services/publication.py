from application.services.base import BaseService

class PublicationService(BaseService):

    def protocol(self) -> str:
        return "https"
    
    def host(self) -> str:
        return "publicationservice.imd.ufrn.br"

    def port(self) -> int:
        return 80
