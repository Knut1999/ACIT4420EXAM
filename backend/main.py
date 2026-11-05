from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from Controller import Controller
from database.fill_db import fill_db


app = FastAPI()
fill_db()
controller = Controller()

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
    budgetType: str 
    budgetSum: float
    preferredDepartureTime: str
    

@app.post("/items/")
async def create_item(item: Item):
    offers = controller.websiteInputs(item.destination,item.budgetType,item.budgetSum, item.preferredDepartureTime)
    result = []
    for offer in offers:
        result.append(offer.__dict__)

    return result