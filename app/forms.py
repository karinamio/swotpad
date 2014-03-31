from flask.ext.wtf import Form, TextField, SubmitField, BooleanField, validators, ValidationError
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class InputForm(Form):
	item = TextField('item', [validators.Required('Invalid entry.')])
	submit = SubmitField('submit')