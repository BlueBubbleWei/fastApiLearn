#__author:  blue
#data:2020/10/23

# http://www.py-edu.com/course/period_detail/58

# uvicorn case4_params:app --reload
from typing import  Optional
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{'item_name': 'foo'}, {'item_name' : 'bar'}, {'item_name': 'Baz'}]

"""
直接参数访问
http://127.0.0.1:8000/items/?skip=1
"""
@app.get('/items/')
async def read_item(skip: int=0, limit: int = 5):
    return fake_items_db[skip: skip + limit]


"""
路径参数访问
http://127.0.0.1:8000/items/4
"""

@app.get("/items/{item_id}")
async def read_item(item_id: str, q:str=None):
    if q:
        return {'item_id': item_id, 'q': q}
    return {'item_id': item_id}

"""
查询参数类型转化
http://127.0.0.1:8000/second_items/3
"""
@app.get('/second_items/{item_id}')
async def read_item(item_id: str, q: str=None, short: bool=False):
    item = {"item_id": item_id}
    if q:
        item.update({'q': q})
    if short:
        item.update({
            'desc': 'dilala'
        })
    return item

"""
多个路径和查询参数
http://127.0.0.1:8000/users/3/items/4
"""

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int, item_id: str, q:str=None, short:bool = False
):
    item = {'item_id': item_id, 'owner_id': user_id}
    if q:
        item.update({'q': q})
    if not short:
        item.update({
            'desc': 'amazing a ha'
        })
    return item

"""
需求查询参数
必须携带needy参数
http://127.0.0.1:8000/items_necessary/3?needy=Yohu
"""
@app.get('/items_necessary/{item_id}')
async def read_user_item(item_id: str, needy: str):
    item = {'item_id': item_id, 'needy': needy}
    return  item

"""
可选的类型声明
http://127.0.0.1:8000/items_Optional/3
http://127.0.0.1:8000/items_Optional/3?limit=3
"""
@app.get('/items_Optional/{item_id}')
async def read_user_item(item_id: str, limit: Optional[int] = None):
    item = {'item_id': item_id, 'limit': limit}
    return item