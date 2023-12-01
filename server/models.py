from fastapi import FastAPI
from pydantic import BaseModel

class WorkItem(BaseModel):
    id: int
    name: str
    price: str
    PerTalk: str
    link: str