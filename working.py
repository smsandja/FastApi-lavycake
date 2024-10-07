from fastapi import FastAPI, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None
class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

inventory = { }
@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]
    
@app.get("/get-by-name")
def get_item(*, name: str = Query(None, title="Name", description="Name of item,"), test: int ):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code=404, detail="Item name not found.")

@app.post("/create-item/{idem_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=400, detail="Item ID already exists")
    inventory[item_id] = item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item : UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=400, detail="Item ID does not exist")
    if inventory[item_id].name != None:
        inventory[item_id].name = item.name

    if inventory[item_id].price != None:
        inventory[item_id].price = item.price

    if inventory[item_id].brand != None:
        inventory[item_id].brand = item.brand  
   
    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id : int = Query(..., description="The ID of the item to delete", lt=0)):
    if item_id not in inventory:
        raise HTTPException(status_code=400, detail="Item ID does not exist")
    
    del inventory[item_id]
    return{"message" : "Item delete with success"}
    



        
