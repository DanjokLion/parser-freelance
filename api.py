from fastapi import FastAPI
from models import *

app = FastAPI()

@app.get('/habr/')
async def get_habr_item(item: HabrItem):
    return item