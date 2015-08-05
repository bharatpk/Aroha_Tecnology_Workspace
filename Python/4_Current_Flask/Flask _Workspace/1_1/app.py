
from flask import Flask , render_template,redirect,request,url_for,session,flash
from functools import wraps 
#import sqlite3
from flask.ext.sqlalchemy import SQLAlchemy




#-------------------------------------
app = Flask(__name__)

'''
import os

app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
'''

app.config.from_object('config.DevelopementConfig')

db = SQLAlchemy(app)

#---------------------------------

def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args,**kwargs)
		else:
			flash('u need to login first')
			return redirect(url_for('login'))
	return wrap




#---------------------------------------
from models import *


@app.route('/')
@login_required
def home():
	#return 'hellow word!! welcome'
	#g.db = connect_db()
	#cur = g.db.execute('select * from po')
	#posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()] 
	#g.db.close()

	posts = db.session.query(BlogPost).all() 

	return render_template('index.html',posts=posts)

#---------------------------------------

	



@app.route('/welcome')

def welcome():
	return render_template("welcome.html")




#----------------------------------------

@app.route('/login' ,methods = ['GET','POST'])

def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] !=  'admin' or  request.form['password'] !=  'admin':
			error = 'Hey its wrong '
		else:
			session ['logged_in'] = True
			flash("You have Just logged_in")
			return redirect (url_for('home'))
	return render_template('login.html',error=error)

#-----------------------------------------


@app.route('/logout')
@login_required

def logout():
	session.pop('logged_in',None)
	
	flash("You have Just Logged Out")
	return redirect(url_for('welcome'))

#-------------------------------------------



#def connect_db():
	#return sqlite3.connect("po.db")






if __name__ == "__main__":
	app.run()






	



