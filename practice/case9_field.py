#__author:  blue
#data:2020/11/4

from fastapi import  Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = Field(None, title='items', max_length=300)
    price: float = Field(..., gt = 4, description='the price must be greater than zero')
    tax: float = None

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body({'price': 8}, embed=True)):
    results ={'item_id': item_id, 'item': item}
    return results

