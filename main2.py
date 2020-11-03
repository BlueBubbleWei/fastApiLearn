from fastapi import FastAPI,Query
import uvicorn
from pydantic import BaseModel
from model import getdata
app = FastAPI(title='测试')



"""
好的学习资料  
http://www.py-edu.com/course/period_detail/91
"""
class BaseItem(BaseModel):
    网站首页地址 : str = None
    网站名称:str = None

class LogItem(BaseModel):
    name : str = None
    eventLog:str = None
    uid: int = 0

@app.post('/postdata')
def get_data(item:BaseItem):
    return getdata().post(item.limit)


@app.get('/getdata/')
def get_data(limit:int = Query(400, description='数据量'),
             网站首页地址:str = Query('baidu',description='网站首页地址')):  # Query传默认参数，还可以设置一些别的内容
    print('>>>', 网站首页地址)
    return getdata().get(网站首页地址)

"""记录bug"""
@app.get('/getLog/')
def get_data(item: LogItem):
    getdata.getLog(item)

if __name__ == '__main__':
    # reload 热加载，修改了自动重启
    uvicorn.run(app='main2:app', reload=True)