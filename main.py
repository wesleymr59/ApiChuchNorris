#!/usr/bin/env python3
from fastapi import FastAPI
from helpers import functions as fun

app = FastAPI()

@app.get("/api/jokes/random",status_code=200)
def random() -> str:
    body = fun.getRandon()
    return body['value']


@app.get("/api/jokes/category/{CATEGORIA}")
def category(CATEGORIA:str) -> dict:
        bodyRequest = fun.getCategoria(CATEGORIA)
        convertBodyRequest = fun.convertTojson(bodyRequest) 
        
        return fun.validaBody(convertBodyRequest)


@app.get("/api/jokes/filter",status_code=200) #?search={query}&limit={limit}
async def filter(search:str | None = None, limit:int =0) -> dict:
    lista = list()
    for i in range(int(limit)):
        
        if search == "random":
            bodyRequest = random()
            lista.append(bodyRequest)

        else:
            bodyRequest = category(search)
            lista.append(bodyRequest)
    return lista