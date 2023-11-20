from fastapi import FastAPI
from models import *
import json, datetime

app = FastAPI()

with open(f'habr_{datetime.datetime.now().strftime("%d_%m_%Y")}.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

@app.get('/habr')
async def get_habr_item():
    return data