from fastapi import FastAPI
from models import *
import json, datetime

app = FastAPI()

with open(f'./storage/habr_{datetime.datetime.now().strftime("%d_%m_%Y")}.json', 'r', encoding='utf-8') as file:
    habr_data = json.load(file)

with open(f'./storage/freelancejob_{datetime.datetime.now().strftime("%d_%m_%Y")}.json', 'r', encoding='utf-8') as file:
    freej_data = json.load(file)


@app.get('/habr')
async def get_habr_item():
    return habr_data

@app.get('/freelancejob')
async def get_freejob_item():
    return freej_data