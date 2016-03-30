# encoding:utf-8

from flask import Flask,render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

#装饰器，根目录

@app.route('/')
def index():
	return render_template('index.html',current_time=datetime.utcnow())
	
#装饰器，用户目录
@app.route('/user/<name>')
def user(name):
	return render_template('user.html',name=name)
	
#装饰器，静态文件
@app.route('/static/')
def sendstatic():
	return render_template('base.html')
	
#装饰器，404 及500
@app.errorhandler(404)
def page_notfound(e):
	return render_template('404.html')
	
@app.errorhandler(500)
def Server_Error(e):
	return render_template('500.html')
	

#主函数
if __name__ == '__main__':
	app.run(debug=True)