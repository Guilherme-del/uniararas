from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from . import models, schemas

async def get_cliente(db: AsyncSession, cliente_id: int):
    result = await db.execute(select(models.Cliente).filter(models.Cliente.id == cliente_id).options(selectinload(models.Cliente.orcamentos)))
    return result.scalars().first()

async def create_cliente(db: AsyncSession, cliente: schemas.ClienteCreate):
    db_cliente = models.Cliente(**cliente.dict())
    db.add(db_cliente)
    await db.commit()
    await db.refresh(db_cliente)
    return db_cliente

async def get_orcamento(db: AsyncSession, orcamento_id: int):
    result = await db.execute(select(models.Orcamento).filter(models.Orcamento.id == orcamento_id))
    return result.scalars().first()

async def create_orcamento(db: AsyncSession, orcamento: schemas.OrcamentoCreate, cliente_id: int):
    db_orcamento = models.Orcamento(**orcamento.dict(), cliente_id=cliente_id)
    db.add(db_orcamento)
    await db.commit()
    await db.refresh(db_orcamento)
    return db_orcamento

async def get_destinos_ordenados(db: AsyncSession, cliente_id: int):
    result = await db.execute(select(models.Orcamento).filter(models.Orcamento.cliente_id == cliente_id).order_by(models.Orcamento.valor_total))
    return result.scalars().all()

async def get_sugestoes_destinos(db: AsyncSession, cliente_id: int):
    result = await db.execute(select(models.Orcamento).filter(models.Orcamento.cliente_id == cliente_id))
    orcamentos = result.scalars().all()
    return random.sample(orcamentos, 2) if len(orcamentos) >= 2 else orcamentos

async def get_orcamentos_por_valor(db: AsyncSession, cliente_id: int, valor_maximo: float):
    result = await db.execute(select(models.Orcamento).filter(models.Orcamento.cliente_id == cliente_id, models.Orcamento.valor_total <= valor_maximo))
    return result.scalars().all()

