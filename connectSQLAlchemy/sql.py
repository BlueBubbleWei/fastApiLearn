#__author:  blue
#data:2020/10/21
"""
学习链接
https://baijiahao.baidu.com/s?id=1666815736028607006&wfr=spider&for=pc

"""


MYSQL_SRVER: str = ''
MYSQL_USER: str = 'root'
MYSQL_PWD = '123456'
MYSQL_DB: str = 'fastapi'
SQLALCHEMY_DATABASE_URL:str = 'mysql+pymysql://root:123456@localhost:3306/fastapi?charset=utf-8'

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Config:
    case_sensitive = True

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping= True)
SessionLocal = sessionmaker(autocommit=False, autoflush= False, bind=engine)


