from fastapi import FastAPI, Depends
from app import auth

app = FastAPI()


@app.get("/", dependencies=[Depends(auth.get_api_key)])
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}", dependencies=[Depends(auth.get_api_key)])
async def say_hello_get(name: str):
    return {"message": f"Hello {name}", "method": "get"}


@app.post("/hello/{name}", dependencies=[Depends(auth.get_api_key)])
async def say_hello_post(name: str):
    return {"message": f"Hello {name}", "method": "post"}
