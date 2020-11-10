
#__author: blue
#data:2020/11/10

from fastapi import FastAPI, status

app = FastAPI()

@app.post('/items/', status_code=201)
async def create_item(name: str):
    return {'name': name}


"""
返回状态码
"""
@app.post('/items2/', status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {'name': name}