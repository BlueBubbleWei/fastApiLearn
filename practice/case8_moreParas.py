#__author: blue
#data:2020/11/4

from fastapi import FastAPI, Path, Query,Body
from pydantic import  BaseModel


app = FastAPI()

class Item(BaseModel):
    name: str
    descrition: str = None
    price: float
    tax:float = None

class User(BaseModel):
    username: str = None
    full_name: str = None


"""
混合Path,Query和请求体参数
"""
@app.put('/items/{item_id}')
async def update_item(
        *,
        item_id: int = Path(..., title='Id', ge=0, le=1000),
        q: str = Query(None, description='查询参数'),
        item: Item = None
        ):
    item.name ='大黑'
    item.price = 32
    item.descrition = 'wahaahha'

    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    if item:
        results.update({'item': item})
    return results

"""
多个请求体参数
"""
@app.put('/items_more/{item_id}')
async def update_item(item_id: int, item: Item, user: User):
    results = {'item_id': item_id, 'item': item, 'user': user}
    return results

"""
body中的奇异值
"""
@app.put('/items_body/{item_id}')
async def update_item(
        item_id: int,
        item: Item,
        user: User,
        importance: int = Body(...)):
    results = {'item_id': item_id, 'item': item, 'user': user, 'importance': importance}
    return results

"""
嵌入单个主体参数
"""
@app.put('/items_single/{item_id}')
async def update_item(item_id: int, item: Item=Body(..., embed=True)):
    results = {'item_id': item_id, 'item': item}
    return results

