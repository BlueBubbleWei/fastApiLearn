#__author:  blue
#data:2020/10/13

import pymysql
import pandas as pd
class getdata():
    def __init__(self):
        # 连接数据库
        self.db = pymysql.connect(host="localhost", user="root",password="123456",database="fastapi",charset="utf8")
        # 创建游标
        # self.cursor = self.db.cursor()

    def post(self,limit):
        # 执行sql语句
        sql = f"select * from zz_info limit {limit}"
        # cursor.execute(' ')
        # 使用pandas操作数据库
        res = pd.read_sql(sql,self.db)
        # records是关键字，可以点进函数里查看注释
        res = res.to_dict('records')
        return res

    def get(self,网站首页地址):
        sql = f"select * from zz_info"
        res = pd.read_sql(sql, self.db)
        print('执行sql语句完成')
        res = res.to_dict('records')
        print('转字典完成')
        return res

    def getLog(self, LogItem):
        cursor = self.db.cursor()
        sql = "INSERT INTO logitem(name, eventLog, uid)values('%s','%s','%d')" % (LogItem.name, LogItem.eventLog, LogItem.uid)
        try:
            cursor.execute(sql)
            self.db.commit()
            return "ok"
        except:
            self.db.rollback()
            return "err"
        # self.db.close()