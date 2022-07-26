from . import db
from flask_login import UserMixin

"""
py
from project import db, create_app, models
db.create_all(app=create_app()) 
"""

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
