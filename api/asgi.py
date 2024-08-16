from fastapi import FastAPI, Request, Query, HTTPException, APIRouter, File, UploadFile
from starlette import status
from starlette.responses import Response, FileResponse
import json


app = FastAPI()
@app.get("/", 
        description="Ахуенно невъебенно крутая отправка ахуенного rest json словаря и точка")
async def root():
    return {"message": "Hello World"}

@app.get("/hello")
async def hello():
    return {"message": "Hello from another route!"}

@app.get("/signup")
async def hello():
    return {"message": "Hello from another route!"}

@app.get("/signin")

async def hello():
    return {"message": "Hello from another route!"}


@app.get("/restore-account-data")
async def hello():
    return {"message": "Hello from another route!"}

@app.get("/account")
async def hello():
    return {"message": "Hello from another route!"}

@app.get("/create-exemption")
async def hello():
    return {"message": "Hello from another route!"}

@app.get("/create-gratitude")
async def hello():
    return {"message": "Hello from another route!"}

@app.get("/files")
async def hello():
    return {"message": "Hello from another route!"}



@app.get("/favicon.ico")
async def favicon():
    return FileResponse("static/favicon.ico")
