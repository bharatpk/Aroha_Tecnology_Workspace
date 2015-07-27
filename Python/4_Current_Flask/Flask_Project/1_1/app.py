from flask import Flask , render_template,redirect,url_for,request

app = Flask(__name__)







@app.route('/welcome')
def welcome():
	return render_template("welcome.html")


@app.route('/')
def home():
	return'welcome'
	

	#return render_template('home.html')


'''
@app.route('/login',methods = ['GET','POST'])
def home():

	return render_template('login.html')
	error = None
	

	if request.method = 'POST':
		if request.from['Username'] != admin or request.from['password'] !=admin:
			error = 'Invalid dude !'
		else:
			return redirect(url_for('home'))




	return render_template('login.html',error=error)

'''






if __name__ == "__main__":
	app.run(debug='True')



	



