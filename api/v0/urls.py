from fastapi import APIRouter, Request,Depends

from apps.codpiece.api.v0 import urls as codpiece_router


router_v0 = APIRouter()
router_v0.include_router(codpiece_router.codpiece_router_v0)