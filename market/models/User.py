from market import db
from flask_sqlalchemy import SQLAlchemy


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    # hashed
    password = db.Column(db.String(length=50), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    # Relationship between two tables. User can own items.
    # owned_user would be an attribute in the 'Item' object
    # Lazy==true => items should be loaded lazily when the property is first accessed
    items = db.relationship('Item', backref='owned_user', lazy=True)

    # method used to represent a class’s objects as a string
    def __repr__(self):
        return f'User {self.username}'


User: SQLAlchemy
