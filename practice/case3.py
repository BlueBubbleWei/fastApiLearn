#__author:  blue
#data:2020/10/23

from fastapi import FastAPI
from enum import  Enum

class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'

app = FastAPI()

@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {'item_id': item_id}

"""
当前接口和下面接口的顺序，会决定返回值，当前接口返回当前用户的信息，下面的接口返回的是查询用户的信息
"""

@app.get('/users/me')
async def read_user_me():
    return {'user)id': 'current user'}

@app.get('/users/{user_id}')
async def read_user(user_id: str):
    return {'user_id': user_id}

"""
返回枚举类型
"""
@app.get('/model/{model_name}')
async def get_model(model_name: ModelName):
    print('>>>>', model_name)
    if model_name == ModelName.alexnet:
        return {'model_name': model_name, 'message': 'deep learning ftw'}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}

"""访问文件"""

@app.get('/files/{file_path: path}')
async def read_file(file_path: str):
    return {'file_path': file_path}


