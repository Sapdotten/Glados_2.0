from fastapi import APIRouter


router_v0 = APIRouter()


@router_v0.get("/", 
        description="Ахуенно невъебенно крутая отправка ахуенного rest json словаря и точка")
async def root():
    return return {"message": "Hello World"}

@router_v0.get("api-v0/codpiece")
async def hello():
    return await 

@router_v0.get("api-v0/codpiece/{id:id}")
async def hello():
    return await 

@router_v0.get("/hello")
async def hello():
    return {"message": "Hello World"}

@router_v0.get("/signup")
async def hello():
    return {"message": "Hello from another route!"}

@router_v0.get("/signin")

async def hello():
    return {"message": "Hello from another route!"}


@router_v0.get("/restore-account-data")
async def hello():
    return {"message": "Hello from another route!"}

@router_v0.get("/account")
async def hello():
    return {"message": "Hello from another route!"}

@router_v0.get("/create-exemption")
async def hello():
    return {"message": "Hello from another route!"}

@router_v0.get("/create-gratitude")
async def hello():
    return {"message": "Hello from another route!"}

@router_v0.get("/files")
async def hello():
    return {"message": "Hello from another route!"}

