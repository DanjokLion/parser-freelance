from fastapi import FastAPI
from models import *
import json, datetime

app = FastAPI()

with open(f'habr_{datetime.datetime.now().strftime("%d_%m_%Y")}.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

@app.post('/habr')
async def get_habr_item(item: HabrItem):
    res = {
        'name': item.name,
        'price': item.price,
        'link': item.link
    }
    return res