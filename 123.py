from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import uvicorn
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.get("/")
def dead_root():
    return {}

class BilliardPlace(BaseModel):
    name: str
    count_table: int  # Изменено на int, так как количество столов не может быть строкой
    price: int

items = {}

@app.get("/items")
def out_items():
    return items

@app.get("/items/{item_id}", response_model=BilliardPlace)
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.post("/items", response_model=BilliardPlace)
async def create_item(item_id: str, item: BilliardPlace):
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item_id] = jsonable_encoder(item)
    return items[item_id]

@app.put("/items/{item_id}", response_model=BilliardPlace)
async def update_item(item_id: str, item: BilliardPlace):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded

@app.delete("/items/{item_id}", response_model=BilliardPlace)
async def delete_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = items[item_id]
    del items[item_id]
    return deleted_item

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
