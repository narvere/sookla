from . import db
from flask_login import UserMixin

"""
py
from sookla_project import db, create_app, models
db.create_all(app=create_app()) 
"""


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    name = db.Column(db.String(1000), unique=True)
    password = db.Column(db.String(100))

    def __repr__(self):
        return f"user: {self.name} with hash: {self.password}"


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    product_name = db.Column(db.String(100), unique=True)
    price = db.Column(db.Float(10))

    def __repr__(self):
        return f"Product: {self.product_name} - {self.price}EUR"