#__author:  blue
#data:2020/11/4

from fastapi import FastAPI,Path,Query

app = FastAPI()
@app.get('/items/{item_id}')
async def read_items(*, item_id: int = Path(..., title='guessMe'), q: str = Query(None, alias='item-query')):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results


"""
数值验证
"""
@app.get('/items_num/{item_id}')
async def read_items(*, item_id: int = Path(..., title='ID', ge=3, description='YOHOoo'), q:str):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results

