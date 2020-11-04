
#__author:  blue
#data:2020/11/4
from typing import List
from fastapi import FastAPI, Query

app = FastAPI()


"""
查询参数
加入q参数的请求 http://127.0.0.1:8000/items/?q=333
"""
@app.get('/items/')
async def read_items(q: str=None):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results

"""
导入查询
"""

@app.get("/items_Query/")
async def read_items(q:str = Query(None, max_length=1)):
    results = {
        'items': [
        {'item_id': 'SB250'}, {'item_id': 'Bar'}
    ],
        'signal': [
        {'item_id': 'SB250'}, {'item_id': 'Bar'}
    ]
    }
    results['len'] = len(results['items'])
    if q:
        results.update({'q': q})
    return results

"""
添加正则表达式
http://127.0.0.1:8000/items_res/?q=fixedquery
不满足http://127.0.0.1:8000/items_res/?q=fixedquery33
"""
@app.get('/items_res/')
async def read_items(q: str = Query(None, min_length=3, max_length=50, regex="^fixedquery$")):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results

"""
添加默认查询参数
Query 中的第一个参数换成...  就会判断参数是否存在，不存在则报错
"""
@app.get('/items_default/')
async def read_items(q: str= Query('fixedquery', min_length=3)):
    results = {'items': [{'item_id': 'foo'}, {'item_id': 'bar'}]}
    if q:
        results.update({'q': q})
    return results

"""
查询参数列表/多个值
"""
@app.get('/items_more/')
async def read_items(q: List[str] = Query(["foo", "bar"])):
    query_items = {'q': q}
    return query_items

"""
查询参数列表/多个值  list替换
"""
@app.get('/items/')
async def read_items(q:list=Query(None) ):
    query_items = {'q': q}
    return query_items

"""
参数别名
http://127.0.0.1:8000/item_alias/?item-query=fixedquery
"""
@app.get('/item_alias/')
async def read_items(q:str = Query(None, alias = 'item-query',deprecated=True)):
    print('q', q)

    results = {'items': [{'item_id': 'doo'}, {'item_id': 'bar'}]}
    results.update({'q': q})
    if q:
        print('ddd')
        results.update({'q': q})
    return results


