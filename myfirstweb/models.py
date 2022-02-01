from datetime import datetime
from myfirstweb import db, login_manager
from flask_login import UserMixin


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(90), unique=True)
	username = db.Column(db.String(30), unique=True)
	password = db.Column(db.String(90))


