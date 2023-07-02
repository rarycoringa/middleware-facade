from __future__ import annotations

from enum import Enum
from typing import Any
from typing import Dict
from typing import List

from pydantic import BaseModel

class AppType(str, Enum):
    GAMES: str = "GAMES"
    SOCIAL_MEDIA: str = "SOCIAL_MEDIA"
    HEAL: str = "HEAL"
    FINANCE: str = "FINANCE"

class SocialMediaType(str, Enum):
    TWITTER: str = "TWITTER"
    LINKEDIN: str = "LINKEDIN"

class SocialMedia(BaseModel):
    type: SocialMediaType
    token: str

class App(BaseModel):
    id: str
    name: str
    type: AppType
    social_medias: List[SocialMedia]
    user_id: str

    @classmethod
    def from_service_format(cls, service_data: Dict[str, Any]) -> App:
        app_data: Dict[str, Any] = {
            "id": service_data["id"],
            "name": service_data["name"],
            "type": service_data["type"],
            "social_medias": service_data["socialMedias"],
            "user_id": service_data["userId"],
        }

    def to_service_format(self) -> Dict[str, Any]:
        service_format: Dict[str, Any] = {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "socialMedias": self.social_medias,
            "userId": self.user_id,
        }

        return service_format

class AppCreation(BaseModel):
    name: str
    type: AppType
    social_medias: List[SocialMedia]
    user_id: str

    def to_service_format(self) -> Dict[str, Any]:
        service_format: Dict[str, Any] = {
            "name": self.name,
            "type": self.type,
            "socialMedias": self.social_medias,
            "userId": self.user_id,
        }

        return service_format