from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'superkarmo'
app.config.from_object('config')

from app import views, models

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/karinamio/Documents/Coding/Projects/swotpad/database.db'

from models import db
db.init_app(app)