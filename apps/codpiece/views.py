from starlette.responses import JSONResponse

from core.views.mixins_class import ModelAPIViewSet 
from apps.codpiece import models as _models


class CodpiecAPIView(ModelAPIViewSet):
    async def list(self):
        instances = await self._list(_models.Codpiece, self.db)
        # print('---> ', instances, type(instances))
        # Преобразование списка экземпляров модели в список словарей
        return JSONResponse([instance.to_dict() for instance in instances])
        
    async def retrieve(self, codpiece_id: int):
        instance = await self._retrieve(_models.Codpiece, self.db, id=codpiece_id)
        # print('---> ', instance, instance.dict(), type(instance))
        return await self.to_json(instance)

    async def create(self, data: dict):
        instance = await self._create(_models.Codpiece, self.db, data)
        return await self.to_json(instance)

    async def update(self, codpiece_id: int, data: dict):
        instance = await self._update(_models.Codpiece, self.db, instance_id=codpiece_id, data=data)
        return await self.to_json(instance)

    async def partial_update(self, codpiece_id: int, data: dict):
        instance = await self._partial_update(_models.Codpiece, self.db, instance_id=codpiece_id, data=data)
        return await self.to_json(instance)

    async def destroy(self, codpiece_id: int):
        response = await self._destroy(_models.Codpiece, self.db, instance_id=codpiece_id)
        return await self.to_json(response)




