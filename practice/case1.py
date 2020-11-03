
#__author:  blue
#data:2020/10/23

"""
在终端通过下面的语句运行
uvicorn case1:app --reload
case1 为文件名
app 为FastAPI实例化的变量名


####
访问文档
http://127.0.0.1:8000/redoc


接口文档
http://127.0.0.1:8000/docs
"""
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "word"}


"""
访问方式
http://127.0.0.1:8000/items/5?q=somequery
"""
@app.get("/items/{item_id}")
def read_item(item_id: int, q:str=None):
    return {'item_id': item_id, 'q': q}

