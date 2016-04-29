# -*- coding: utf8 -*-


## 将股票信息写入 stock_basics 表中


import tushare as ts
from sqlalchemy import create_engine

df = ts.get_stock_basics()
engine = create_engine('mysql://root:123456@127.0.0.1/test?charset=utf8')

df.to_sql('stock_basics',engine,if_exists='append')