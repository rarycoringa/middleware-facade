from __future__ import annotations

import datetime

from typing import Dict
from typing import Any

from pydantic import BaseModel

    
class Publication(BaseModel):
    id = int
    user_id = str
    status = bool
    published_at = datetime.datetime
    text = str
    summary = str

    @classmethod
    def from_service_format(cls, service_data: Dict[str, Any]) -> Publication:
        publication_data: Dict[str, Any] = {
            "id": service_data["pubId"],
            "user_id": service_data["user"],
            "status": service_data["status"],
            "published_at": service_data["publishedAt"],
            "text": service_data["text"],
            "summary": service_data["summary"],
        }

        return cls.parse_obj(publication_data)
