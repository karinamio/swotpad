from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class InputForm(Form):
	item = TextField('item', validators = [Required()])
