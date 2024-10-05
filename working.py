from fastapi import FastAPI

app = FastAPI()

inventory = {
        1: {
            "name" : "Riz",
            "price" : 2000,
            "brand" : "regular"
        },
        2: {
            "name" : "Pate",
            "price" : 1500,
            "brand" : "regular"
        },
        3: {
            "name" : "Patato",
            "price" : 1500,
            "brand" : "regular"
        }
    }
@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]
    
@app.get("/get-by-name")
def get_item(name: str):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not found"}


    



        
