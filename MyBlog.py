# encoding:utf-8

import time
from flask import Flask,render_template


app = Flask(__name__)

@app.route('/user/<name>')
def user(name):
	mydict = {'key':'flask'}
	mylist = [1,2,3,'myintvar',5]
	comments = ['Python2.7','Python3.0']
	return render_template('user.html', name=name, mydict=mydict , mylist=mylist,comments=comments )
	
if __name__ == '__main__':
	app.run(debug=True)