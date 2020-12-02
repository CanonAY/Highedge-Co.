from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all backend logic that interacts with database and other services
"""

def get_user(email):
    """
    Get a user by a given email
    :param email: the email of the user
    :return: a user that has the matched email address
    """
    user = User.query.filter_by(email=email).first()
    return user


def login_user(email, password):
    """
    Check user authentication by comparing the password
    :param email: the email of the user
    :param password: the password input
    :return: the user if login succeeds
    """
    # if this returns a user, then the name already exists in database
    user = get_user(email)
    if not user or not check_password_hash(user.password, password) or not email == user.email:
        return None
    return user

def register_user(email, name, password, password2, balance):
    """
    Register the user to the database
    :param email: the email of the user
    :param name: the name of the user
    :param password: the password of user
    :param password2: another password input to make sure the input is correct
    :return: an error message if there is any, or None if register succeeds
    """

    hashed_pw = generate_password_hash(password, method='sha256')
    # store the encrypted password rather than the plain password
    # initial balance set to the integer passed as parameter, which is always 5000. 
    new_user = User(email=email, name=name, password=hashed_pw, balance=balance)

    db.session.add(new_user)
    db.session.commit()
    return new_user


# retrieve all tickets information stored in database.
def get_all_tickets():
    return Ticket.query.all()

    
# When we buy a new ticket, this helps us to update the quantity of new available ticket on the current page
def get_ticket(name):
    ticket = Ticket.query.filter_by(name = name).first()
    return ticket

# This stores the new ticket for selling into the database
def new_ticket_for_sell(name, email, quantity, price, date):
    """
    Create new ticekt for selling by user
    :param name: ticket name for sell
    :param quantity: ticket quantity for sell
    :param price: ticket price for sell
    :param date: ticket expiratation date for sell
    """
    new_ticket = Ticket(name=name, owner_email=email, quantity=quantity, price=price, date=date)
    db.session.add(new_ticket)
    db.session.commit()
    return new_ticket

# This method updates the ticket information
def update_ticket(name, email, quantity, price, date):
    """
    Change ticket information
    :param name: ticket name for sell
    :param quantity: ticket quantity for sell
    :param price: ticket price for sell
    :param date: ticket expiratation date for sell
    """
    # Find target ticket in database, and delete it. 
    Ticket.query.filter(Ticket.name == name).delete()
    # Then add a new ticket to the database, with same name but modified information. 
    new_ticket = Ticket(name=name, owner_email=email, quantity=quantity, price=price, date=date)
    db.session.add(new_ticket)
    db.session.commit()
    return new_ticket