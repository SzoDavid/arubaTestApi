from fastapi import FastAPI, Depends
from app import auth
from app.dto.requests import NameReq

app = FastAPI()


@app.get("/", dependencies=[Depends(auth.get_api_key)])
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}", dependencies=[Depends(auth.get_api_key)])
async def say_hello_get(name: str):
    return {"message": f"Hello {name}", "method": "get"}


@app.post("/hello", dependencies=[Depends(auth.get_api_key)])
async def say_hello_post(name_req: NameReq):
    return {"message": f"Hello {name_req.name}", "method": "post"}
