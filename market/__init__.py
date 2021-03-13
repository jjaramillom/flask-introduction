from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

db.init_app(app)
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/
app.app_context().push()

from market import routes
