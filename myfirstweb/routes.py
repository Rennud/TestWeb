
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

routes = Blueprint('routes', __name__)



@routes.route('/')
@routes.route('/home')
def home():
	return render_template('home.html')


@routes.route('/about')
def about():
	return render_template('about.html')