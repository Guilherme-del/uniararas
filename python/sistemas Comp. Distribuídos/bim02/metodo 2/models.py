from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    celular = Column(String, index=True)
    email = Column(String, index=True)
    orcamentos = relationship("Orcamento", back_populates="cliente")

class Orcamento(Base):
    __tablename__ = "orcamentos"
    id = Column(Integer, primary_key=True, index=True)
    destino = Column(String, index=True)
    valor_passagem = Column(Float)
    quantidade_passagens = Column(Integer)
    valor_total = Column(Float)
    data_cadastro = Column(String)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))

    cliente = relationship("Cliente", back_populates="orcamentos")