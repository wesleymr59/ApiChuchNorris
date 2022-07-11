#!/usr/bin/env python3
from fastapi import FastAPI
from routers import random, category, filtery


app = FastAPI()

app.include_router(random.router)
app.include_router(category.router)
app.include_router(filtery.router)
