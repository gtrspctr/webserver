from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

"""
class Note(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Data = db.Column(db.String(10000))
    Date = db.Column(db.DateTime, default=func.now())
    UserId = db.Column(db.Integer, db.ForeignKey('user.Id'), nullable=False)

class User(db.Model, UserMixin):
    Id = db.Column(db.Integer, primary_key=True)
    Email = db.Column(db.String(256), unique=True, nullable=False)
    FirstName = db.Column(db.String(256), nullable=False)
    LastName = db.Column(db.String(256), nullable=False)
    Password = db.Column(db.String(256), nullable=False)
    Notes = db.relationship('Note', backref='author', lazy=True)
    Date = db.Column(db.DateTime, default=func.now())

    def __repr__(self):
        return f"User('{self.FirstName}', '{self.LastName}', '{self.Email}')"
    
"""

class RemoteRequests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(15), nullable=False)
    method = db.Column(db.String(7), nullable=False)
    agent = db.Column(db.String(256), nullable=False)