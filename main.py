import logging
from typing import Union


import os, sys, time
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

logger = logging.getLogger("__name__")

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


if __name__ == "__main__":
    try:
        logger.info("""FastAPI Start ... """)
        uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)
    except Exception as e:
        logger.error(f"❌ FastAPI start filed: {e}")
