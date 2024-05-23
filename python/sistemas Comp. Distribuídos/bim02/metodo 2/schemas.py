from pydantic import BaseModel
from typing import List, Optional

class OrcamentoBase(BaseModel):
    destino: str
    valor_passagem: float
    quantidade_passagens: int
    valor_total: float
    data_cadastro: str

class OrcamentoCreate(OrcamentoBase):
    pass

class Orcamento(OrcamentoBase):
    id: int
    cliente_id: int

    class Config:
        orm_mode = True

class ClienteBase(BaseModel):
    nome: str
    celular: str
    email: str

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int
    orcamentos: List[Orcamento] = []

    class Config:
        orm_mode = True
