from fastapi import FastAPI, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str]

inventory = {
        1: {
            "name" : "Riz",
            "price" : 2000,
            "brand" : "regular"
        }
    }
@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]
    
@app.get("/get-by-name")
def get_item(*, name: str = Query(None, title="Name", description="Name of item,"), test: int ):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not found"}

@app.get("/create-item")
def create_item(item: Item):
    return{}

    



        
