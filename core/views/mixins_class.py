from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeMeta

from core.views.get_or_404 import get_list_or_404, get_object_or_404
from core.views.viewsets import BaseAPIView


class ListModelMixin(BaseAPIView):
    async def _list(self, model: DeclarativeMeta, db: AsyncSession, **kwargs):
        return await self.handle_errors(lambda: get_list_or_404(model, db, **kwargs))

class RetrieveModelMixin(BaseAPIView):
    async def _retrieve(self, model: DeclarativeMeta, db: AsyncSession, **kwargs):
        return await self.handle_errors(lambda: get_object_or_404(model, db, **kwargs))

class CreateModelMixin(BaseAPIView):
    async def _create(self, model: DeclarativeMeta, db: AsyncSession, data: dict):
        return await self.handle_errors(lambda: self._create_instance(model, db, data))
    
    async def _create_instance(self, model: DeclarativeMeta, db: AsyncSession, data: dict):
        instance = model(**data)
        db.add(instance)
        await db.commit()
        await db.refresh(instance)
        return instance

class UpdateModelMixin(RetrieveModelMixin):
    async def _update(self, model: DeclarativeMeta, db: AsyncSession, instance_id: int, data: dict):
        return await self.handle_errors(lambda: self._update_instance(model, db, instance_id, data))

    async def _update_instance(self, model: DeclarativeMeta, db: AsyncSession, instance_id: int, data: dict):
        instance = await self._retrieve(model, db, id=instance_id)
        for key, value in data.items():
            setattr(instance, key, value)
        db.add(instance)
        await db.commit()
        await db.refresh(instance)
        return instance

    async def _partial_update(self, model: DeclarativeMeta, db: AsyncSession, instance_id: int, data: dict):
        return await self.handle_errors(lambda: self._partial_update_instance(model, db, instance_id, data))

    async def _partial_update_instance(self, model: DeclarativeMeta, db: AsyncSession, instance_id: int, data: dict):
        instance = await self._retrieve(model, db, id=instance_id)
        for key, value in data.items():
            if value is not None:  # Check if the value is not None
                setattr(instance, key, value)
        db.add(instance)
        await db.commit()
        await db.refresh(instance)
        return instance

class DestroyModelMixin(RetrieveModelMixin):
    async def _destroy(self, model: DeclarativeMeta, db: AsyncSession, instance_id: int):
        return await self.handle_errors(lambda: self._destroy_instance(model, db, instance_id))

    async def _destroy_instance(self, model: DeclarativeMeta, db: AsyncSession, instance_id: int):
        instance = await self._retrieve(model, db, id=instance_id)
        await db.delete(instance)
        await db.commit()
        return {"message": f"{model.__name__} deleted"}


class ModelAPIViewSet( 
        CreateModelMixin,
        ListModelMixin,
        UpdateModelMixin,
        DestroyModelMixin
    ):
    pass

class ReadOnlyViewSet( 
        RetrieveModelMixin,
        ListModelMixin,
    ):
    pass