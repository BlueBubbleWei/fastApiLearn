#__author:  blue
#data:2020/11/10

from typing import List
from fastapi import Cookie, Header, FastAPI
app = FastAPI()

@app.get('/items/')
async def read_items(*, ads_id: str= Cookie(None)):
    return {'ads_id': ads_id}

@app.get('/items2/')
async def read_items(*, user_agent: str =Header(None)):
    return {'uSER-Agent': user_agent}

"""
禁用下划线自动转换为连字符，请将Header的参数convert_underscores设置为False
"""
@app.get('/items4/')
async def read_items(*, strange_header: str = Header(None, convert_underscores=False)):
    return {"strange_header": strange_header}

"""
要声明可以多次出现的X-Token标头
"""
@app.get('/items5/')
async def read_items(x_token: List[str] = Header(None)):
    return {'X-token values': x_token}



