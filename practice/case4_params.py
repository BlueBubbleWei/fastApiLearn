#__author:  blue
#data:2020/10/23

# http://www.py-edu.com/course/period_detail/58

# uvicorn case4_params:app --reload

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{'item_name': 'foo'}, {'item_name' : 'bar'}, {'item_name': 'Baz'}]

"""
直接参数访问
"""
@app.get('/items/')
async def read_item(skip: int=0, limit: int = 0):
    return fake_items_db[skip: skip + limit]


"""
路径参数访问
"""

@app.get("/items/{item_id}")
async def read_item(item_id: str, q:str=None):
    if q:
        return {'item_id': item_id, 'q': q}
    return {'item_id': item_id}

"""
查询参数类型转化
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