from typing import Optional

from pydantic import BaseModel

class App(BaseModel):
    id: str
    name: str
    cpf: Optional[str]
    cnpj: Optional[str]