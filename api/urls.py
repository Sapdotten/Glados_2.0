from fastapi import FastAPI, HTTPException, Depends
from starlette import status
from starlette.requests import Request
import subprocess

from api.user_api import api_router

app = FastAPI()  # noqa: pylint=invalid-name

app.include_router(api_router)


def start():
    subprocess.call('uvicorn api.urls:app --reload', shell=True)


