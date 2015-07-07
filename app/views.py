from flask import render_template
from app import app 

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/me')
def front():
	return render_template('front.html')