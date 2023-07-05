from __future__ import annotations

from typing import Any
from typing import Dict
from typing import ByteString

from pydantic import BaseModel
from pydantic import Field

class TwitterIDs(BaseModel):
    user_id: str
    twitter_user_id: str

    def to_service_format(self) -> Dict[str, Any]:
        service_format: Dict[str, Any] = {
            "idUsuario": self.user_id,
            "idUsuarioTwitter": self.twitter_user_id,
        }

        return service_format
    
class TwitterGraphics(BaseModel):
    user_id: str
    graph_likes_by_post: bytes
    graph_average_likes_by_day: bytes
    graph_retweets_by_post: bytes
    graph_followers_progress: bytes
    graph_relation_followers_and_favorites: bytes
    graph_relation_between_retweets_and_favorites: bytes
    graph_replies_by_post: bytes
    graph_replies_by_day: bytes

    @classmethod
    def from_service_format(cls, service_data: Dict[str, Any]) -> TwitterGraphics:
        twitter_graphics_data: Dict[str, Any] = {
            "user_id": service_data["idUsuario"],
            "graph_likes_by_post": service_data["GraficoLikesPorPostagem"],
            "graph_average_likes_by_day": service_data["GráficoLinhaMediaLikesPorDia"],
            "graph_retweets_by_post": service_data["GraficoDeRetweetsPorPost"],
            "graph_followers_progress": service_data["GraficoDeProgressãoDeSeguidores"],
            "graph_relation_followers_and_favorites": service_data["GraficoDeFavoritosEmRelaçãoASeguidores"],
            "graph_relation_between_retweets_and_favorites": service_data["GraficoDeRelacaoEntreRetweetsEFavoritos"],
            "graph_replies_by_post": service_data["GraficoDeRepliesPorPostagem"],
            "graph_replies_by_day": service_data["GraficoDeRepliesPorDia"],
        }

        return cls.parse_obj(twitter_graphics_data)

        


