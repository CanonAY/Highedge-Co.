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
        error_message = "The passwords do not match"

    elif len(email) < 1:    # email cannot be empty
        error_message = "Email format error"
        
    elif not (parseaddr(email)[1] == email and '@' in parseaddr(email)[1] and '.' in parseaddr(email)[1]):
        error_message = "Email does not follow addr-spec defined in RFC 5322"

    elif len(password) < 6:
        error_message = "Password has to be at least 6 characters"
        
    elif len(name) <= 2:
        error_message = "User name has to be longer than 2 characters"
        
    elif len(name) >= 20:
        error_message = "User name has to be less than 20 characters"
        
    elif not name.isalnum():
        error_message = "User name has to be alphanumeric"
    
    elif name[0] == ' ' or name[-1] == ' ':
        error_message = "Space allowed only if it is not the first or the last character"
    
    else:
        user = bn.get_user(email)
        if user:
            error_message = "User exists"        
    
    password_complexity = False

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
        error_message = "Password has to meet the required complexity: at least one upper case, at least one lower case, and at least one special character"
            
    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message != None:
        return render_template('register.html', message=error_message)
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
            email_in_rfc5322 = True;

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
            return render_template('login.html', message='password/email format is incorrect.')
        elif not password_meet_complexity:
            return render_template('login.html', message='password/email format is incorrect.')
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
    tickets = bn.get_all_tickets()
    return render_template('index.html', user=user, tickets=tickets)
