from fastapi import APIRouter, Request,Depends

from apps.codpiece.views import CodpiecAPIView 
from apps.codpiece import schemas as _schemas


codpiece_router_v0 = APIRouter()

@codpiece_router_v0.post("/codpieces/", response_model=_schemas.Codpiece)
async def create_codpiece(codpiece: _schemas.CodpieceCreate, manager: CodpiecAPIView = Depends(CodpiecAPIView.create_session)):
    return await manager.create(codpiece.dict())

@codpiece_router_v0.get("/codpieces/{codpiece_id}", response_model=_schemas.Codpiece)
async def retrieve_codpiece(codpiece_id: int, manager: CodpiecAPIView = Depends(CodpiecAPIView.create_session)):
    return await manager.retrieve(codpiece_id)

@codpiece_router_v0.get("/codpieces/", response_model=list[_schemas.Codpiece])
async def list_codpieces(manager: CodpiecAPIView = Depends(CodpiecAPIView.create_session)):
    return await manager.list()

@codpiece_router_v0.put("/codpieces/{codpiece_id}", response_model=_schemas.Codpiece)
async def update_codpiece(codpiece_id: int, codpiece: _schemas.CodpieceUpdate, manager: CodpiecAPIView = Depends(CodpiecAPIView.create_session)):
    return await manager.update(codpiece_id, codpiece.dict())

@codpiece_router_v0.patch("/codpieces/{codpiece_id}", response_model=_schemas.Codpiece)
async def partial_update_codpiece(codpiece_id: int, codpiece: _schemas.CodpieceUpdate, manager: CodpiecAPIView = Depends(CodpiecAPIView.create_session)):
    return await manager.partial_update(codpiece_id, codpiece.dict())

@codpiece_router_v0.delete("/codpieces/{codpiece_id}")
async def destroy_codpiece(codpiece_id: int, manager: CodpiecAPIView = Depends(CodpiecAPIView.create_session)):
    return await manager.destroy(codpiece_id)