from flask import render_template, flash, redirect
from app import app
from forms import InputForm
import random

@app.route('/')
@app.route('/index')
@app.route('/submit.html', methods = ['GET', 'POST'])
def submit():
	form = InputForm()
	if form.validate_on_submit():
		flash('Item requested=' + form.item.data)
		return redirect('/submit.html')
	return render_template("submit.html", form = form)

@app.route('/generate.html')
def generate():
	posts = ['wash face', 'flush toilet','eat cheese']
	message = random.choice(posts)
	return render_template("generate.html", message = message)

@app.route('/report.html')
def report():
	return render_template("report.html")

@app.errorhandler(404)
def not_found(error):
	return render_template('error.html'), 404