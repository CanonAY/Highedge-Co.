from flask import render_template, request, session, redirect
from qa327 import app
import qa327.backend as bn
from email.utils import parseaddr

"""
This file defines the front-end part of the service.
It elaborates how the services should handle different
http requests from the client (browser) through templating.
The html templates are stored in the 'templates' folder. 
"""


@app.route('/register', methods=['GET'])
def register_get():
    # templates are stored in the templates folder
    if 'logged_in' in session:
        return redirect('/', code = 303)    # has logged in, redirect to / page
    else:
        return render_template('register.html', message='')    # show registration page
    

@app.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    error_message = None


    if password != password2:    # password and password2 have to be exactly the same
        error_message = "Password"

    elif len(email) < 1:    # email cannot be empty
        error_message = "Email"
        
    elif not (parseaddr(email)[1] == email and '@' in parseaddr(email)[1] and '.' in parseaddr(email)[1]):
        error_message = "Email"

    elif len(password) < 6:
        error_message = "Password"
        
    elif len(name) <= 2:
        error_message = "User name"
        
    elif len(name) >= 20:
        error_message = "User name"
        
    elif not name.isalnum():
        error_message = "User name"
    
    elif name[0] == ' ' or name[-1] == ' ':
        error_message = "User name"

            
    password_complexity = False
    password_lower = False
    password_upper = False
    password_symbol = False

    # check if the password meet the complexity requirements
    for c in password:
        if c.islower():
            password_lower = True
        elif c.isupper():
            password_upper = True
        elif c in "!@#$%^&*()-+?_=,<>/":
            password_symbol = True
            
    # If the password meets all complexity requirements, then the password is valid. 
    if password_lower and password_upper and password_symbol: 
        password_complexity = True

    if password_complexity is False:
        error_message = "Password"
            
    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message != None:
        return render_template('login.html', message='{} format is incorrect.'.format(error_message))
    else:
        user = bn.get_user(email)
        if user:
            return render_template('login.html', message='this email has been ALREADY used.')
        else:
            # When there is no error message, create new user, with balance initialized to 5000. 
            bn.register_user(email, name, password, password2, 5000)
            # Registration succeed, redirect to login page. 
            return redirect('/login')


@app.route('/login', methods=['GET'])
def login_get():
    # If the user already logged in, redirect to profile. 
    if 'logged_in' in session:
        return redirect('/', code=303);
    else:
        return render_template('login.html', message='Please login')

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    user = bn.login_user(email, password)

    if user:
        session['logged_in'] = user.email
        """
        Session is an object that contains sharing information 
        between browser and the end server. Typically it is encrypted 
        and stored in the browser cookies. They will be past 
        along between every request the browser made to this services.

        Here we store the user object into the session, so we can tell
        if the client has already login in the following sessions.

        """
        # success! go back to the home page
        # code 303 is to force a 'GET' request
        return redirect('/', code=303)
    else:
        email_in_rfc5322 = False
        password_meet_complexity = False
        password_length = False
        password_lower = False
        password_upper = False
        password_symbol = False
        # Check if the email follows RFC5322 standard
        if parseaddr(email)[1] == email and '@' in parseaddr(email)[1] and '.' in parseaddr(email)[1] :
            email_in_rfc5322 = True

        # Check if the length of password meets requirement
        if len(password) >= 6:
            password_length = True
        # Check if the password meets requirement: contains lowercase, contains uppercase, contains special character
        for c in password:
            if c.islower():
                password_lower = True
            elif c.isupper():
                password_upper = True
            elif c in "!@#$%^&*()-+?_=,<>/":
                password_symbol = True
        
        # If the password meets all complexity requirements, then the password is valid. 
        if password_length and password_lower and password_upper and password_symbol: 
            password_meet_complexity = True

        # If either of the email or password doesn't meet format requirements, 
        # then show error message to tell user login failed because of format problem.  
        if not email_in_rfc5322:
            return render_template('login.html', message='email/password format is incorrect.')
        elif not password_meet_complexity:
            return render_template('login.html', message='email/password format is incorrect.')
        # If login failed for other reasons, that means password doesn't match the email. 
        else:
            return render_template('login.html', message='email/password combination incorrect')


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')


def authenticate(inner_function):
    """
    :param inner_function: any python function that accepts a user object

    Wrap any python function and check the current session to see if 
    the user has logged in. If login, it will call the inner_function
    with the logged in user object.

    To wrap a function, we can put a decoration on that function.
    Example:

    @authenticate
    def home_page(user):
        pass
    """

    def wrapped_inner():

        # check did we store the key in the session
        if 'logged_in' in session:
            email = session['logged_in']
            user = bn.get_user(email)
            if user:
                # if the user exists, call the inner_function
                # with user as parameter
                return inner_function(user)
        else:
            # else, redirect to the login page
            return redirect('/login')

    # return the wrapped version of the inner_function:
    return wrapped_inner


@app.route('/')
@authenticate
def profile(user):
    # authentication is done in the wrapper function
    # see above.
    # by using @authenticate, we don't need to re-write
    # the login checking code all the time for other
    # front-end portals

    # Get all tickets' info from backend. 
    tickets_infor = bn.get_all_tickets_infor()
    all_name = []
    all_price = []
    all_quantity = []
    all_email = []
    # Add all information to corresponding collumn. 
    for ticket in tickets_infor:
        all_name.append(ticket[0])
        all_price.append(ticket[1])
        all_quantity.append(ticket[2])
        all_email.append(ticket[3])
    # Pass all information to the HTML page. 
    return render_template('index.html', user = user, names = all_name, prices = all_price, quantities = all_quantity, emails = all_email)




@app.route('/sell', methods=['POST'])
def sell_post():
    # Get current user's email, with is the ticket owner's email. 
    email = session['logged_in']
    user = bn.get_user(email)

    # Get ticket information from post form. 
    name = request.form.get('sell-name')
    quantity = int(request.form.get('sell-quantity'))
    price = int(request.form.get('sell-price'))
    date = request.form.get('sell-date')

    # The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.
    # The name of the ticket is no longer than 60 characters
    name_valid = False
    if name.isalnum() and name[0] != " " and name[-1] != " " and len(name) >= 6 and len(name) <= 60:
        name_valid = True

    # The quantity of the tickets has to be more than 0, and less than or equal to 100.
    quantity_valid = False
    if quantity > 0 and quantity <= 100:
        quantity_valid = True

    # Price has to be of range [10, 100]
    price_valid = False
    if price >= 10 and price <= 100:
        price_valid = True

    # Date must be given in the format YYYYMMDD (e.g. 20200901)
    date_valid = False
    # If the format is correct, two '-' character will be added at index 4 and 7. 
    if len(date) == 10 and date[4] == '-' and date[7] == '-' :
        date_valid = True

    # Check if the name of ticket doesn't exist in database. 
    name_unique = False
    ticket = bn.get_ticket(name)
    if not ticket:
        name_unique = True

    # If all elements have valid format, then ticket information is valid, redirect to sell page and show message. 
    if name_valid and quantity_valid and price_valid and date_valid and name_unique:
        ticket = bn.new_ticket_for_sell(name, email, quantity, price, date)
        return render_template('sell.html', message_s = "Ticket successfully posted", ticket_name = name, ticket_quantity = quantity, ticket_price = price, ticket_date = date)
    # For any errors, redirect back to / and show an error message.
    else:
        return render_template('index.html', message_s = "Ticket format invalid", user=user)

    
@app.route('/buy', methods=['POST'])
def buy_post():

    #Get into current user's account to proceed buying process
    email = session['logged_in']
    user = bn.get_user(email)

    #Get the name and quantity from the buying form
    name = request.form.get('buy-name')
    quantity = int(request.form.get('buy-quantity'))

    # the name of the ticket has to be alphanumeric-only and space is allowed with requirements
    name_valid = False
    if name.isalnum() and name[0] != " " and name[-1] != " ":
        name_valid = True

    # the name of the ticket is no longer than 60 characters
    name_len = False
    if len(name) <= 60 and len(name) >=6:
        name_len = True

    # quantity of ticket is within the range 0(disclusive) to 100(inclusive)
    quantity_valid = False
    if quantity > 0 and quantity <= 100:
        quantity_valid = True

    # ticket name does not exsit in the database
    ticket_exist = False
    #check the ticket name from the backend
    ticket = bn.get_ticket(name)
    if ticket:
        ticket_exist = True 

    # ticket has more quantaties than required to buy
    quantity_require = False
    if quantity <= ticket.quantity:
        quantity_require = True

    # user has more balance than the ticket price * quantity + service fee (35%) + tax(5%)
    required_price = int(ticket.price) * int(ticket.quantity) * (1 + 0.35 + 0.05)
    balance_valid = False
    if user.balance >= required_price:
        balance_valid = True 
            
    # if there is no error in the buying form 
    if name_valid and name_len and quantity_valid and ticket_exist and quantity_require and balance_valid:
        return render_template('buy.html', message_b = "Ticket successfully posted", ticket_name = name, ticket_quantity = quantity)

    #there is error(s) in the buying form 
    else: 
        return render_template('index.html', message_b = "Ticket format invalid", user=user)



