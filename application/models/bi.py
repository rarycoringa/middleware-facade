from __future__ import annotations

from typing import Any
from typing import Dict 

from pydantic import baseModel 

class IDs(baseModel):
    user_id = str 
    twitter_user_id = str

    def formater_of_request(self) -> Dict[str, any]:
        formater_of_request = Dict[str, any] = {
            "idUsuario": self.user_id,
            "twitter_user_id": self.twitter_user_id,
        }

        return formater_of_request

    
class Dashboard_data:
    user_id = str
    graph_likes_by_post = str
    graph_average_likes = str

    @classmethod
    def formater_of_response(cls, service_data:Dict[str, any]) -> Dashboard_data:
        dashboard_data = Dict[str, any] = {
            "user_id": service_data["idUsuario"],
            "graph_likes_by_post": service_data["GraficoLikesPorPostagem"],
            "graph_average_likes": service_data["GráficoLinhaMediaLikesPorDia"],
        }

        return cls.parse_obj(dashboard_data)

        


