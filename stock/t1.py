# -*- coding: utf8 -*-

from sqlalchemy import create_engine
import tushare as ts

df = ts.get_hist_data('600848', start='2014-01-01')
engine = create_engine('mysql://root:123456@127.0.0.1/test?charset=utf8')

#df['code']='600848'
#存入数据库
#df.to_sql('hist_data',engine,if_exists='append')

print df

#追加数据到现有表
#df.to_sql('tick_data',engine,if_exists='append')

