from fastapi import FastAPI
from pydantic import BaseModel

class HabrItem(BaseModel):
    name: str
    price: str
    link: str