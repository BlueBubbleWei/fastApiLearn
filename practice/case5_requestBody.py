#__author: blue
#data:2020/11/4

from fastapi import  FastAPI
from pydantic import BaseModel


# 导入pydantic的基本模型
# 创建你的数据模型
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


app = FastAPI()


""""
发起一个post请求
测试 http://127.0.0.1:8000/docs#/default/create_item_items__post
"""
@app.post('/items/')
async def create_item(item: Item):
    item.name = '大黑'
    item_dict= item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({
            'price_with_tax': price_with_tax
        })
    return item_dict

"""
请求体+路径+查询参数
"""
@app.put('/items/{item_id}')
async def create_item(item_id: int, item: Item, q: str = None):
    result = {'item_id': item_id, **item.dict()}
    if q:
        result.update({'q': q})
    return result






