from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
	__tablename__ = 'info'
	key = db.Column(db.Integer, primary_key = True)
	item = db.Column(db.String(150))

	def __init__(self, item):
		self.item = item

	def __repr__(self):
		return "<Item('%s')>" % (self.item)	