#__author:  blue
#data:2020/11/10

from typing import Set
from fastapi import  FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


"""
找不到时的异常处理
"""
@app.get('/items/{item_id}')
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {'item': items[item_id]}

"""
添加自定义头
"""
@app.get('/items-header/{item_id}')
async def read_item_header(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail='Item not found',
            headers={"X-Error": "There goes my error"}
        )
    return {'item': items[item_id]}


"""
安装自定义异常处理
"""
from fastapi import Request
from fastapi.responses import JSONResponse

class UnicornEXception(Exception):
    def __init__(self, name: str):
        self.name = name



@app.exception_handler(UnicornEXception)
async def unicorn_exceptio_handler(request: Request, exc: UnicornEXception):
    return JSONResponse(
        status_code=418,
        content= {"message": f"Oops! {exc.name} did something. There goes a rainbow..."}
    )

@app.get('/unicorns/{name}')
async def read_unicorn(name: str):
    if name == 'yoyo':
        raise UnicornEXception(name=name)
    return {"unicorn_name": name}




########################

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: Set[str] = []

@app.post("/items2/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(*, item: Item):
    return item



"""
下面的注释可以添加到文档上
"""
@app.post("/items3/", response_model=Item, summary="Create an item")
async def create_item(*, item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item

fake_db = {}
@app.put("/items4/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data