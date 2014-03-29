from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class Item(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	message = db.Column(db.String(150))

	def __init__(self, message):
		self.message = self.message

	# instructing Python how to print objects of this class
	def __repr__(self):
		return '<Item %r>' % (self.message)