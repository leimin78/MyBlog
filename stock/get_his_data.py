
# -*- coding: utf8 -*-

import tushare as ts
import MySQLdb
from sqlalchemy import create_engine

#连接数据库
db = MySQLdb.connect("127.0.0.1","root","123456","test")
cursor = db.cursor()

#查询数据库，获取股票代码及，上市时间
select_code_sql = "select code,timeTomarket from stock_basics where timeTomarket <> 0"
cursor.execute(select_code_sql)
code_resluts = cursor.fetchall()

#循环遍历每一个code
for row in code_resluts:
    print u"股票代码：%s,上市时间：%s" %(row[0],row[1])

    #获取每一个股票的历史数据
    df = ts.get_hist_data(row[0],row[1])

    #将股票代码新增到原有数据
    df['code'] = row[0]

    #将数据追加到现有表
    engine = create_engine('mysql://root:123456@127.0.0.1/test?charset=utf8')
    df.to_sql('hist_data',engine,if_exists='append')

db.close()
