from fastapi import APIRouter
from starlette import status
from starlette.responses import Response
import json

api_router = APIRouter()


@api_router.post("/check")
async def release():
    return Response(status_code=status.HTTP_200_OK, content = json.dumps({'message':'hello'}))
