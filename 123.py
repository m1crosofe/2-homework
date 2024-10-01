from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI
import uvicorn
from fastapi.encoders import jsonable_encoder
from typing import Union

app = FastAPI()


@app.get("/")
def dead_root():
    return {"Введите в строке /shaurma-adress   или /shaurma-names"}


class billiard_place(BaseModel):
    name: str
    count_table: str
    price: int


items = {}


@app.get("/items")
def out_items():
    return items


@app.get("/items/{item_id}", response_model=billiard_place)
async def read_item(item_id: str):
    return items[item_id]


@app.put("/items/{item_id}", response_model=billiard_place)
async def update_item(item_id: str, item: billiard_place):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
