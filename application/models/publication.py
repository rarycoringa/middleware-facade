from __future__ import annotations

from typing import Dict

from datetime import datetime
from pydantic import BaseModel

    
class Publication(BaseModel):
    pub_id = int 
    user = str
    status = bool
    created_at = datetime
    text = str 
    summary = str

    @classmethod
    def formater_of_response(cls, service_data:Dict[str, any]) -> Publication:
        publication_info = Dict[str, any] = {
            "pub_id": service_data["PublicationId"],
            "user": service_data["User"],
            "status": service_data["Status"],
            "created_at": service_data["CreatedAt"],
            "text": service_data["Text"],
            "summary": service_data["Summary"],
        }

        return publication_info
