from __future__ import annotations

from typing import Any
from typing import Dict 

from pydantic import BaseModel

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
    graph_average_likes: bytes

    @classmethod
    def from_service_format(cls, service_data: Dict[str, Any]) -> TwitterGraphics:
        twitter_graphics_data: Dict[str, Any] = {
            "user_id": service_data["idUsuario"],
            "graph_likes_by_post": service_data["GraficoLikesPorPostagem"],
            "graph_average_likes": service_data["GráficoLinhaMediaLikesPorDia"],
        }

        return cls.parse_obj(twitter_graphics_data)

        


