#__author:  blue
#data:2020/11/9

from fastapi import FastAPI,Body
from  pydantic import  BaseModel,Field
app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }


class Item2(BaseModel):
    name: str = Field(..., example="fool")
    description: str = Field(None, example='A very nice Item')
    price: float = Field(..., example = 35.4)
    tax: float = Field(None, example = 3.2)

@app.put("/items/{item_id}")
async def update_item(*, item_id: int, item: Item):
    results = {'item_id': item_id, 'item': item}
    return results


"""
返回对象的默认值
"""
@app.put("/items2/item_id")
async def update_item(*, item_id: int, item: Item2):
    results = {'item_id': item_id, 'item': item}
    return  results

"""
另一种默认传值的方式
"""

class Item3(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


@app.put('/item3/{item_id}')
async def update_item(*, item_id: int, item: Item3 = Body(
    ...,
    example = {
        'name': 'Fool',
        'decription': 'A very nice Item',
        'price': 35.4,
        'tax': 3.23
    }
)):
    results = {'item_id': item_id, 'item': item}
    return results




