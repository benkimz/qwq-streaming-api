from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from huggingface_hub import InferenceClient

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

class Message(BaseModel):
    role: str
    content: str

class Query(BaseModel):
    messages: list[Message]
    temperature: float = 0.5
    max_tokens: int = 10200
    top_p: float = 0.7
    stream: bool = False


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}