from fastapi import FastAPI
from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient('mongodb://localhost:27017/')

db = client['mainDB']
collection = db['mainCollection']

app = FastAPI()

@app.get('/orders')
async def read_data():
    data = await collection.find().to_list()
    return data

