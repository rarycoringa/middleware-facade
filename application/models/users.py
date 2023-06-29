from __future__ import annotations

from enum import Enum
from typing import Any, Union
from typing import Dict

from pydantic import BaseModel
from pydantic import validator

CPF_LENGTH: int = 11
CNPJ_LENGTH: int = 14

class DocumentType(str, Enum):
    CPF: str = "CPF"
    CNPJ: str = "CNPJ"

class Document(BaseModel):
    type: DocumentType
    number: str

    @validator("number")
    def number_validator(cls, value: str, values: Dict[str, Any]) -> str:
        type: DocumentType = values.get("type")

        allowed_length: int = CPF_LENGTH if type == DocumentType.CPF else CNPJ_LENGTH

        if len(value) != allowed_length:
            raise ValueError(f"a \'{type.value}\' must have exactly {allowed_length}.")
        
        return value

class AccountUserMixin:
    @property
    def cpf(self: Union[User, UserCreation]) -> str:
        return self.document.number if self.document.type == DocumentType.CPF else None

    @property
    def cnpj(self: Union[User, UserCreation]) -> str:
        return self.document.number if self.document.type == DocumentType.CNPJ else None

class User(BaseModel, AccountUserMixin):
    id: str
    name: str
    document: Document

    @classmethod
    def from_service_format(cls, service_data: Dict[str, Any]) -> User:
        user_data: Dict[str, Any] = {
            "id": service_data["id"],
            "name": service_data["name"],
            "document": {
                "type": DocumentType.CPF if service_data["cpf"] is not None else DocumentType.CNPJ,
                "number": service_data["cpf"] if service_data["cpf"] is not None else service_data["cnpj"],
            }
        }
        return cls.parse_obj(user_data)
        

    def to_service_format(self) -> Dict[str, Any]:
        service_format: Dict[str, Any] = {
            "id": self.id,
            "name": self.name,
            "cpf": self.cpf,
            "cnpj": self.cnpj,
        }

        return service_format

class UserCreation(BaseModel, AccountUserMixin):
    name: str
    document: Document

    def to_service_format(self) -> Dict[str, Any]:
        service_format: Dict[str, Any] = {
            "name": self.name,
            "cpf": self.cpf,
            "cnpj": self.cnpj,
        }

        return service_format