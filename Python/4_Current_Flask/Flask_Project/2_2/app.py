from flask import Flask , render_template
#-------------------------------------
app = Flask(__name__)




@app.route('/')
def home():
	#return 'welcome'
	return render_template("home.html")



@app.route('/welcome')

def welcome():
	return render_template("welcome.html")

@app.route('/website_trafic_trends')

def websitetrafictrends():
	return render_template("website_trafic.html")


@app.route('/sales')

def salesfun():
	return render_template("sales.html")




if __name__ == "__main__":
	app.run(debug='True')




