from flask import render_template, flash, redirect, request, url_for
from app import app
from forms import InputForm
from models import db, Item
import random

@app.route('/')
@app.route('/index')
@app.route('/load', methods = ['GET', 'POST'])
def load():
	form = InputForm()
	if request.method == 'POST':
		if form.validate() == False:
			flash ('Invalid entry.')
			return render_template("load.html", form = form)
		else: 
			newitem = Item(form.item.data)
			db.session.add(newitem)
			db.session.commit()
			flash ('Added' + " " + '"' + form.item.data + '"' + " to the swotpad.")
			return redirect('/load')	
	elif request.method == 'GET':
		return render_template("load.html", form = form)

@app.route('/deploy')
def deploy():
	items = db.session.query(Item.item).all()
	if not items: 
		return render_template ("deploy.html", item = 'you gotta load up the swotpad first')
	else:
		randomizer = random.choice(items)
		item = randomizer.item
		return render_template("deploy.html", item = item)

@app.route('/report')
def report():
	return render_template("report.html")

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
	return render_template('500.html'), 404