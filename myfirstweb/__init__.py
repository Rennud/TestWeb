from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


app = Flask(__name__)
db = SQLAlchemy()
DB_NAME = "database.db"
app.config['SECRET_KEY'] = 'dafsjkfsjkdfnasdjflbsda'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)


login_manager = LoginManager(app)
login_manager.login_view = 'routes.login'
login_manager.init_app(app)


from .routes import routes
from .auth import auth

app.register_blueprint(routes, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')

from .models import User

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))

if not path.exists('/testweb' + DB_NAME):
	db.create_all(app=app)
	print('New DB')