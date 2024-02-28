from typing import Optional

from fastapi import FastAPI
from requests import *
app = FastAPI()


@app.get("/")
async def root():
    return get("https://icanhazip.com/").text

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
