from fastapi import APIRouter
from helpers import functions as fun

router = APIRouter(prefix="/teste")

@router.get("/api/jokes/filter",status_code=200) #?search={query}&limit={limit}
async def filter(search:str | None = None, limit:int =0) -> dict:
    lista = list()
    for i in range(int(limit)):
        
        if search == "random":
            bodyRequest = fun.getRandon()
            lista.append(bodyRequest)

        else:
            bodyRequest = fun.buscaPorParametros(search)
            lista.append(bodyRequest)
    return lista