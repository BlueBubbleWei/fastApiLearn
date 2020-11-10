# __author:  blue
# data:2020/11/10

from typing import Union, List, Dict
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: str = None


class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type = 'car'


class PlaneItem(BaseItem):
    type = 'plane'
    size: int


items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    }
}


def fake_password_hasher(raw_password: str):
    return 'supersecret' + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print('userSaerf! not really')
    return user_in_db


@app.post('/user/', response_model=UserOut)
async def create_user(*, user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved


"""
Union或anyOf 意味着该响应将是两种类型中的任何一种
"""


@app.get('/items4/{item_id}', response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: str):
    return items[item_id]


"""
返回对象列表
"""


class Item4(BaseModel):
    name: str
    description: str


items4 = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]


@app.get('/items4/', response_model=List[Item4])
async def read_items():
    return items4


"""
带有任意dict的响应
"""

@app.get('/keyword-weights/', response_model=Dict[str, float])
async def red_keyword_weights():
    return {"foo": 2.3, "bar": 3.4}