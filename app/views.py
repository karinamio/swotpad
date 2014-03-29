from flask import render_template, flash, redirect, request, url_for
from app import app
from forms import InputForm
from models import db
import random

@app.route('/')
@app.route('/index')
@app.route('/submit.html', methods = ['GET', 'POST'])
def submit():
	form = InputForm()
	if request.method == 'POST':
		if form.validate() == False:
			flash ('Invalid entry.')
			return render_template("submit.html", form = form)
		else: 
			flash ('Added' + " " + '"' + form.item.data + '"' + " to the swotpad.")
			return redirect('/submit.html')	
	elif request.method == 'GET':
		return render_template("submit.html", form = form)

@app.route('/generate.html')
def generate():
	posts = ['wash face', 'flush toilet','eat cheese']
	message = random.choice(posts)
	return render_template("generate.html", message = message)

@app.route('/report.html')
def report():
	return render_template("report.html")

@app.route('/testdb')
def testdb():
	if db.session.query("1").from_statement("SELECT 1").all():
		return 'It works.'
	else:
		return "Something is broken."	

@app.errorhandler(404)
def not_found(error):
	return render_template('error.html'), 404