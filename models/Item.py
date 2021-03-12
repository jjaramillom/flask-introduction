from flask_sqlalchemy import SQLAlchemy
from shared.models import db


class Item(db.Model):
    def __init__(self, db: SQLAlchemy):
        self.name = db.Column(db.String(length=30))
