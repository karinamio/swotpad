from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
	__tablename__ = 'items'
	key = db.Column(db.Integer, primary_key = True)
	item = db.Column(db.String(150))
	category = db.Column(db.String(15))

	def __init__(self, item, category):
		self.item = item
		self.category = category