from dataclasses import dataclass
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from config.settings import async_session_factory

from apps.codpiece import models as _models
from apps.codpiece import schemas as _schemas

@dataclass
class CodpiecAPIView:
    db: AsyncSession

    @classmethod
    async def create_session(cls):
        db = await async_session_factory().__aenter__()
        instance = cls(db)
        try:
            yield instance
        finally:
            await db.__aexit__(None, None, None)

    async def get_or_404(self, codpiece_id: int):
        query = select(_models.Codpiece).where(_models.Codpiece.id == codpiece_id)
        result = await self.db.execute(query)
        db_codpiece = result.scalars().first()
        if db_codpiece is None:
            raise HTTPException(status_code=404, detail="Codpiece not found")
        return db_codpiece

    async def list(self):
        query = select(_models.Codpiece)
        result = await self.db.execute(query)
        return result.scalars().all()

    async def retrieve(self, codpiece_id: int):
        return await self.get_or_404(codpiece_id)

    async def create(self, data: dict):
        codpiece = _schemas.CodpieceCreate(**data)
        db_codpiece = _models.Codpiece(**codpiece.dict())
        self.db.add(db_codpiece)
        await self.db.commit()
        await self.db.refresh(db_codpiece)
        return db_codpiece

    async def update(self, codpiece_id: int, data: dict):
        codpiece = _schemas.CodpieceUpdate(**data)
        db_codpiece = await self.get_or_404(codpiece_id)
        for var, value in vars(codpiece).items():
            setattr(db_codpiece, var, value) if value else None
        self.db.add(db_codpiece)
        await self.db.commit()
        await self.db.refresh(db_codpiece)
        return db_codpiece

    async def partial_update(self, codpiece_id: int, data: dict):
        codpiece = _schemas.CodpieceUpdate(**data)
        db_codpiece = await self.get_or_404(codpiece_id)
        for var, value in vars(codpiece).items():
            setattr(db_codpiece, var, value) if value else None
        self.db.add(db_codpiece)
        await self.db.commit()
        await self.db.refresh(db_codpiece)
        return db_codpiece

    async def destroy(self, codpiece_id: int):
        db_codpiece = await self.get_or_404(codpiece_id)
        await self.db.delete(db_codpiece)
        await self.db.commit()
        return {"message": "Codpiece deleted"}