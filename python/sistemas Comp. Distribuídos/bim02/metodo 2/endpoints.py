from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
import random

from . import crud, models, schemas
from .database import get_db

router = APIRouter()

@router.post("/clientes/", response_model=schemas.Cliente)
async def create_cliente(cliente: schemas.ClienteCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_cliente(db=db, cliente=cliente)

@router.get("/clientes/{cliente_id}", response_model=schemas.Cliente)
async def read_cliente(cliente_id: int, db: AsyncSession = Depends(get_db)):
    db_cliente = await crud.get_cliente(db, cliente_id=cliente_id)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")
    return db_cliente

@router.post("/clientes/{cliente_id}/orcamentos/", response_model=schemas.Orcamento)
async def create_orcamento_for_cliente(
    cliente_id: int, orcamento: schemas.OrcamentoCreate, db: AsyncSession = Depends(get_db)
):
    return await crud.create_orcamento(db=db, orcamento=orcamento, cliente_id=cliente_id)

@router.get("/clientes/{cliente_id}/destinos/", response_model=List[schemas.Orcamento])
async def read_destinos_ordenados(cliente_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.get_destinos_ordenados(db=db, cliente_id=cliente_id)

@router.get("/clientes/{cliente_id}/sugestoes/", response_model=List[schemas.Orcamento])
async def read_sugestoes_destinos(cliente_id: int, db: AsyncSession = Depends(get_db)):
    return await crud.get_sugestoes_destinos(db=db, cliente_id=cliente_id)

@router.get("/clientes/{cliente_id}/orcamentos/", response_model=List[schemas.Orcamento])
async def read_orcamentos_por_valor(cliente_id: int, valor_maximo: float, db: AsyncSession = Depends(get_db)):
    return await crud.get_orcamentos_por_valor(db=db, cliente_id=cliente_id, valor_maximo=valor_maximo)
