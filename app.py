from flask import Flask, render_template, redirect, request
import joblib

# __name__ = __main__
app = Flask(__name__)

model=joblib.load('model.pkl')

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/',methods=['POST'])
def marks():
	if request.method=='POST':
		hours=float(request.form['hours'])
		marks=str(model.predict([[hours]])[0][0])

	return render_template("index.html",get_marks=marks)

@app.route('/home', methods = ['POST'])
def home():
	return redirect('/')

	
if __name__ == '__main__':
	#Reflects changes when we refresh the page
	#app.debug = True
	app.run(debug=True)

	
