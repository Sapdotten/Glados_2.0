from fastapi import FastAPI,StaticFiles

from api.v0.urls import router_v0 

app = FastAPI()

app.include_router(router_v0)


