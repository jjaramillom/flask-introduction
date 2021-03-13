from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '3c81070f775a7e7ac6a67c22'

db.init_app(app)
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/
app.app_context().push()

from market import routes
