#第一个自建Blog，基于 Python + Flask
#记录Python学习的过程

#2016年3月30日，发布到亚马逊主机

python 虚拟环境 venv

服务端 wsgi

前端代理 nginx


#2016年3月31日，新加入表单功能 及IP查询功能,表单使用flask-wtf IP查询调用淘宝接口

小纪要:

1.浏览器刷新时会调用最后一个post请求，对最后一个post请求需重定向。


#2016年4月4日，学习使用flask-sqlalchemy 组件操作数据库

同时学习sqlite3 轻量级数据库的安装使用。


#2016年4月5日，使用sqlalchemy 操作数据库，sqlalchmy 将表映射成对象

python操作对象即可操作表。


更新点，新增 /static/及test.html

小纪要 对于windows平台 数据库 url 地址 需使用 '/' 而不能使用windows的‘\’

#2016年4月6日，使用flask-mail 发送邮件，博客新增功能
点击我会记住你，博主将收到自动的邮件提醒。

#4月12日 将邮件发送改为异步发送

#4月24日 新增config.py 封装配置文件，对文件结构做调整

#4月29日 重构，加入 stock 数据分析分之，实现功能 获取所有股票历史数据，及输出近1个月各股的涨跌幅

