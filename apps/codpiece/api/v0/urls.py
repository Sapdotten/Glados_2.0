from fastapi import APIRouter, Depends, Request

from apps.codpiece.views import CodpiecAPIView #starletteCodpiecAPIView
from apps.codpiece import forms as _forms


codpiece_router_v0 = APIRouter()

# можно делать так через декораторы как предлагает fastAPI,
# а можно по нормальному как предлагает starlette см.ниже.
@codpiece_router_v0.get("/codpieces/", response_model=list[_forms.Codpiece])
async def list_codpieces(
    manager: CodpiecAPIView = Depends(CodpiecAPIView.create_session)
    ):
    """Получить список всех Codpieces."""
    return await manager.list()

@codpiece_router_v0.get("/codpieces/{codpiece_id}", response_model=_forms.Codpiece)
async def retrieve_codpiece(
        codpiece_id: int,
        manager: CodpiecAPIView = Depends(CodpiecAPIView.create_session)
    ):
    """Получить Codpiece по его ID."""
    return await manager.retrieve(codpiece_id)

@codpiece_router_v0.post("/codpieces/", response_model=_forms.Codpiece)
async def create_codpiece(
        data: _forms.CodpieceCreate,  # Используем модель для создания
        manager: CodpiecAPIView = Depends(CodpiecAPIView.create_session)
    ):
    """Создать новый Codpiece."""
    return await manager.create(data.dict())  # Передаем данные в виде dict

@codpiece_router_v0.put("/codpieces/{codpiece_id}", response_model=_forms.Codpiece)
async def update_codpiece(
        codpiece_id: int, 
        data: _forms.CodpieceUpdate,
        manager: CodpiecAPIView = Depends(CodpiecAPIView.create_session)
    ):
    """Обновить существующий Codpiece."""
    return await manager.update(codpiece_id, data.dict())  # Передаем данные в виде dict

@codpiece_router_v0.patch("/codpieces/{codpiece_id}", response_model=_forms.Codpiece)
async def partial_update_codpiece(
        codpiece_id: int, 
        data: _forms.CodpieceUpdate,
        manager: CodpiecAPIView = Depends(CodpiecAPIView.create_session)
    ):
    """Частично обновить существующий Codpiece."""
    return await manager.partial_update(codpiece_id, data.dict())  # Передаем данные в виде dict

@codpiece_router_v0.delete("/codpieces/{codpiece_id}")
async def destroy_codpiece(
        codpiece_id: int, 
        manager: CodpiecAPIView = Depends(CodpiecAPIView.create_session)
    ):
    """Удалить Codpiece по его ID."""
    return await manager.destroy(codpiece_id)
    



# вариант stralette
# routes = [
#     Route("/codpieces/", starletteview.list, methods=["POST"]),
#     Route("/codpieces/{codpiece_id}", starletteview.retrieve, methods=["GET"]),
#     Route("/codpieces/", list_codpieces, methods=["GET"]),
#     Route("/codpieces/{codpiece_id}", starletteview.update, methods=["PUT"]),
#     Route("/codpieces/{codpiece_id}", starletteview.partial_update, methods=["PATCH"]),
#     Route("/codpieces/{codp iece_id}", starletteview.destroy, methods=["DELETE"]),
# ]


# db = CodpiecAPIView()
# #помесь stralette\django\fastAPI крч франкештейн 
# codpiece_router_v0.add_api_route("/codpieces/",
#                                  CodpiecAPIView.create, 
#                                  methods=["POST"],
#                                  response_model=_forms.CodpieceCreate
#                                 )
# codpiece_router_v0.add_api_route("/codpieces/{codpiece_id}", 
#                                  CodpiecAPIView.retrieve, 
#                                  response_model=_forms.CodpieceCreate,
#                                  methods=["GET"],
#                                 )
# codpiece_router_v0.add_api_route("/codpieces/", 
#                                  CodpiecAPIView.list,
#                                  methods=["GET"],
#                                  response_model=list[_forms.CodpieceUpdate]
#                                 )
# codpiece_router_v0.add_api_route("/codpieces/{codpiece_id}", 
#                                  CodpiecAPIView.update,
#                                  methods=["PUT"],
#                                  response_model=_forms.CodpieceUpdate
#                                 )
# codpiece_router_v0.add_api_route("/codpieces/{codpiece_id}", 
#                                  CodpiecAPIView.partial_update,
#                                  methods=["PATCH"],
#                                  response_model=_forms.CodpieceUpdate
#                                 )
# codpiece_router_v0.add_api_route("/codpieces/{codpiece_id}",
#                                  CodpiecAPIView.destroy,
#                                  methods=["DELETE"],
                                 
#                                 )



