from fastapi import FastAPI
from models import *
# import json, datetime
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker


app = FastAPI()

#Соединение с бд
engine = create_engine('sqlite:///maindb.db')

# Сессия на время соединения с бд
Session = sessionmaker(bind=engine)
session = Session()

#Определение таблицы, с которой читаются данные
metadata = MetaData()
table = Table('jobs', metadata, autoload_with=engine)

#Определил эндпоинт, для получения данных, и возвращаю их в виде списка словарей
@app.get('/jobs')
async def get_data():
    return [dict(row) for row in session.query(table).all()]


# with open(f'./storage/habr_{datetime.datetime.now().strftime("%d_%m_%Y")}.json', 'r', encoding='utf-8') as file:
#     habr_data = json.load(file)

# with open(f'./storage/freelancejob_{datetime.datetime.now().strftime("%d_%m_%Y")}.json', 'r', encoding='utf-8') as file:
#     freej_data = json.load(file)


# @app.get('/habr')
# async def get_habr_item():
#     return habr_data

# @app.get('/freelancejob')
# async def get_freejob_item():
#     return freej_data