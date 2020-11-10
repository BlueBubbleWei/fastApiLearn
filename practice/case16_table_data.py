
#__author:  blue
#data:2020/11/10

from fastapi import FastAPI,Form, File, UploadFile
app = FastAPI()


"""
表单数据
"""
@app.post('/login/')
async def login (*, username: str = Form(...), password: str = Form(...)):
    return {'username': username}

"""
请求文件
"""
@app.post('/files/')
async def create_file(file: bytes = File(...)):
    return {'file_size': len(file)}

"""
上传文件
"""
@app.post('/uploadfile/')
async def create_upload_file(file: UploadFile = File(...)):
    return {'filename': file.filename}


"""
请求表单和文件
"""
@app.post('/files2/')
async def create_file(file: bytes =File(...), fileb: UploadFile = File(...), token:str = Form(...)):
    return {
        'file_size': len(file),
        'token': token,
        'file_content_type': fileb.content_type
    }



