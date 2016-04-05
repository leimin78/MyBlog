﻿# encoding:utf-8

from flask import Flask,render_template,session,redirect,url_for,flash,request
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import SubmitField,StringField
from wtforms.validators import required
from flask.ext.sqlalchemy import SQLAlchemy
import RealIP
import dbconfig


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#初始化Flask 实例，添加秘钥，数据库参数配置
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = dbconfig.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = dbconfig.SQLALCHEMY_COMMIT_ON_TEARDOWN

#实例化数据库对象
db = SQLAlchemy(app)

#实例化bootstrap模板对象
bootstrap = Bootstrap(app)

#实例化moment对象
moment = Moment(app)

#定义表单类
class NameForm(Form):
	name = StringField('请告诉我你的名字？',validators=[required()])
	Submit = SubmitField('我会记住你的')

#定义ROLE,USER模型
class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	users = db.relationship('User', backref='role')
	def __repr__(self):
		return '<Role %r>' % self.name

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, index=True)
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
	def __repr__(self):
		return '<User %r>' % self.username

#装饰器，根目录,传入方法GET,POST供表单使用
@app.route('/',methods=['GET','POST'])
def index():
	form = NameForm()
	IP = request.remote_addr
	attribution = RealIP.ip_location(IP)
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('你的输入有变化哦 :)')
		session['name'] = form.name.data
		return redirect(url_for('index'))
	return render_template("index.html",current_time=datetime.utcnow(),name=session.get('name'),form=form,IP=IP,attribution=attribution)
	
#装饰器，用户目录
@app.route('/user/<name>')
def user(name):
	return render_template('user.html',name=name)
	
#装饰器，静态文件
@app.route('/static/')
def sendstatic():
	return render_template('base.html')

@app.route('/test/')
def test():
	form = NameForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.name.data).first()
		if user is None:
			user = User(username = form.name.data)
			db.session.add(user)
			session['known'] = False
		else:
			session['known'] = True
		session['name'] = form.name.data
		form.name.data = ''
		return redirect(url_for('test'))
	return render_template('test.html',form = form, name = session.get('name'),known = session.get('known', False))

#装饰器，404 及500
@app.errorhandler(404)
def page_notfound(e):
	return render_template('404.html')
	
@app.errorhandler(500)
def Server_Error(e):
	return render_template('500.html')
	

#主函数
if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)