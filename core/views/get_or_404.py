from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import DeclarativeMeta

# shortcuts 
async def get_object_or_404(model: DeclarativeMeta, db: AsyncSession, **kwargs):
    query = select(model).filter_by(**kwargs)
    result = await db.execute(query)
    instance = result.scalars().first()
    if instance is None:
        raise HTTPException(status_code=404, detail=f"No {model.__name__} matches the given query.")
    return instance

async def get_list_or_404(model: DeclarativeMeta, db: AsyncSession, **kwargs):
    query = select(model).filter_by(**kwargs)
    result = await db.execute(query)
    instance = result.scalars().all()

    if instance is None:
        raise HTTPException(status_code=404, detail=f"No {model.__name__} matches the given query.")
    return instance