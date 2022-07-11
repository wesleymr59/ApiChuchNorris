from fastapi import APIRouter
from helpers import functions as fun

router = APIRouter(prefix="/teste")

@router.get("/api/jokes/random",tags=['random'],status_code=200)
def random() -> str:
    body = fun.getRandon()
    return body['value']
