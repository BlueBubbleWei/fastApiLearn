
#__author:  blue
#data:2020/11/10

from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags: List[str] = []

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None


@app.post('/items/', response_model=Item)
async def create_item(item: Item):
    return item

@app.post('/user/', response_model=UserIn)
async def create_user(*, user: UserIn):
    return user

@app.post('/user2/', response_model=UserOut)
async def create_user(*, user: UserIn):
    return user


"""
响应模型参数编码
"""

class Item2(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = 10.5
    tags: List[str] = []

items = {
    "foo": {"name": 'Foo', "price": 50.2},
    "bar": {"name": 'Bar', 'description': 'The bartenders', 'price': 62, 'tax': 20.2},
    'baz': {'name': 'Baz', 'description': None, 'price': 50.2, 'tax': 10.5, 'tags': []}
}

# 传foo bar baz
@app.get("/items3/{item_id}", response_model=Item2, response_model_exclude_unset=True)
async def read_item(item_id: str):
    print(items[item_id], '>>>')
    return items[item_id]

# 装饰器参数response_model_include和response_model_exclude。 它们使用带有属性名称的一组str来包括（省略其余部分）或排除
@app.get('/items/{item_id}/name', response_model=Item2, response_model_include={'name', 'description'})
async def read_item_name(item_id: str):
    return items[item_id]

@app.get('/items/{item_id}/public', response_model=Item2, response_model_exclude={'tax'})
async def read_item_public_data(item_id: str):
    return items[item_id]