from qa327 import app
from flask_sqlalchemy import SQLAlchemy

"""
This file defines all models used by the server
These models provide us a object-oriented access
to the underlying database, so we don't need to 
write SQL queries such as 'select', 'update' etc.
"""


db = SQLAlchemy()
db.init_app(app)


class User(db.Model):
    """
    A user model which defines the sql table
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    # Add a new entry, balance in class User
    balance = db.Column(db.Integer)

#Ziyu Yang, I added a new ticke database 
class Ticket(db.Model):
    """
    A ticket model which defines the sql table
    """
    name = db.Column(db.String(1000), primary_key=True)
    owner_email= db.Column(db.String(1000))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    date = db.Column(db.Integer)
    
# it creates all the SQL tables if they do not exist
with app.app_context():
    db.create_all()
    db.session.commit()
