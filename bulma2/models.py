from . import db

"""
py
from bulma2 import db, create_app, models
db.create_all(app=create_app()) 
"""


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
