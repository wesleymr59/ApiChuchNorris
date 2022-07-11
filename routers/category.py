from fastapi import APIRouter
from helpers import functions as fun

router = APIRouter(prefix="/category")

@router.get("/api/jokes/category/{CATEGORIA}")
def category(CATEGORIA:str) -> dict:

    return fun.buscaPorParametros(CATEGORIA)