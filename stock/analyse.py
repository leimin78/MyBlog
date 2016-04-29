# -*- coding: utf8 -*-

import MySQLdb
import datetime
import collections

#创建数据库对象
db = MySQLdb.connect("127.0.0.1","root","123456","test")
cursor = db.cursor()

#获取当前日期1月前的日期

d = datetime.datetime.now()
dayscount = datetime.timedelta(days = d.day)
dayto = d - dayscount
start_time = dayto.strftime("%Y-%m-%d")

#查询出1月前的数据，股票代码，及涨跌幅
code_sql = "select code,p_change from hist_data where date" +">="+ "'"+start_time+"'"
print code_sql
cursor.execute(code_sql)
reslut = cursor.fetchall()

#对结果进行遍历，获取每一个代码近一个月涨跌幅显示每一个股票近期的涨跌幅
tmp = {}

'''for row in reslut:
    tmp[row[0]] = tmp.get(row[0]) and tmp[row[0]] + row[1] or row[1]
reslut= [ [k, row] for (k, row) in tmp.items() ]
'''

data = collections.defaultdict(float)

for code,values in reslut:
    data[code] += values

for row in data.items():
    print u"股票代码:%s，最近1个月涨跌幅：%s " % (row[0],row[1])

db.close()