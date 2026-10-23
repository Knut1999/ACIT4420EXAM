from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.fill_db import fill_db


fill_db()
app = FastAPI()

origins = [
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET", "POST"],
)

@app.get("/hello")
def read_root():
    return {"Hello": "World"}



class Item(BaseModel):
    destination: str
    budget: str 

@app.post("/items/")
async def create_item(item: Item):
    return item