Test Data:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)

test_form = Form(
    email = '', 
    password = ''
)

test_email = Email(
    local_part = "test",
    at = "@",
    domain_name = "test.com"
)

test_ticket = Ticket(
    owner = 'test_frontend@test.com',
    name = 'test_ticket_yo',
    quantity = 10,
    price = 10,
    date = '20200901'
)

test_date = Date(
    year = "2000"
    month = "01"
    date  = "01"

)
```

##### Test case R1.1: If the user hasn't logged in, show the login page

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - validate that current page contains `#email` element
 - validate that current page contains `#password` element

##### Test case R1.2: the login page has a message that by default says 'please login'

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - validate that current page contains `#login-reminder` element
 - validate the text field of `#login-reminder` element is 'please login'

##### Test case R1.3: If the user has logged in, redirect to the user profile page

Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element input `[type="submit"]`
 - open /login again
 - validate that current page contains `#welcome-header` element

##### Test case R1.4: The login page provides a login form which requests two fields: email and passwords

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - validate that current page contains `#email` element
 - validate that current page contains `#password` element

##### Test case R1.5: The login form can be submitted as a POST request to the current URL (/login)

Mocking:
 - Mock backend.get_user to return a test_user instance
 - Mock backend.get_form to return a test_form instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element input `[type="submit"]`
 - validate that the value of `test_form.email` is identical to the text field of `#email`  
 - validate that the value of `test_form.password` is identical to the text field of `#password`

##### Test case R1.6: Email and password both cannot be empty - positive

Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element input `[type="submit"]`
 - validate that current page contains `#welcome-header` element

##### Test case R1.6: Email and password both cannot be empty - negative

Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - click element input `[type="submit"]`
 - validate that current page contains `#message` element
 - validate the text field of `#message` element is 'email field and password field cannot be empty'
 - enter test_user's email into element `#password`
 - click element input `[type="submit"]`
 - validate that current page contains `#message` element
 - validate the text field of `#message` element is 'email field and password field cannot be empty'

##### Test case R1.7: Email has to follow addr-spec defined in RFC 5322 - positive

Mocking:
 - Mock backend.get_email to return a test_email instance
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element input `[type="submit"]`
 - validate that current page contains `#welcome-header` element

##### Test case R1.7: Email has to follow addr-spec defined in RFC 5322 - negative

Mocking:
 - Mock backend.get_email to return a test_email instance
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_email's local_part into element `#email`
 - enter test_user's password into element `#password`
 - click element input `[type="submit"]`
 - validate that current page contains `#message` element
 - validate the text field of `#message` element is 'please enter a valid email'
 - enter test_email's local_part+at into element `#email`
 - click element input `[type="submit"]`
 - validate that current page contains `#message` element
 - validate the text field of `#message` element is 'please enter a valid email'
 - enter test_email's at+domain_name into element `#email`
 - click element input `[type="submit"]`
 - validate that current page contains `#message` element
 - validate the text field of `#message` element is 'please enter a valid email' 


##### Test case R1.8: Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character - positive

Mocking:
 - Mock backend.get_email to return a test_email instance
 - Mock backend.get_password to return a test_password instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element input `[type="submit"]`
 - validate that current page contains `#welcome-header` element


##### Test case R1.8: Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character - negative

Mocking:
 - Mock backend.get_email to return a test_email instance
 - Mock backend.get_password to return a test_password instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter "12aB*" into element `#password`
 - click element input `[type="submit"]`
 - validate that current page contains `#message` element
 - validate the text field of `#message` element is 'password must meet complexity requirement' 
 - enter "123ab*" into element `#password`
 - click element input `[type="submit"]`
 - validate that current page contains `#message` element
 - validate the text field of `#message` element is 'password must meet complexity requirement' 
 - enter "123BC*" into element `#password`
 - click element input `[type="submit"]`
 - validate that current page contains `#message` element
 - validate the text field of `#message` element is 'password must meet complexity requirement' 
 - enter "123abC" into element `#password`
 - click element input `[type="submit"]`
 - validate that current page contains `#message` element
 - validate the text field of `#message` element is 'password must meet complexity requirement' 


##### Test case R1.9: For any formatting errors, render the login page and show the message 'email/password format is incorrect.'

Mocking:
 - Mock backend.get_password to return a test_password instance
 - Mock backend.get_email to return a test_email instance
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_email's local_part into element `#email`
 - enter test_user's password into element `#pasword`
 - click element input `[type="submit"]`
 - validate current page contains element `render`
 - validate current page contains text "email/password format is incorrect."
 - enter test_user's email into element `#email`
 - enter test_password's invalid_1 into element `#pasword`
 - click element input `[type="submit"]`
 - validate current page contains element `render`
 - validate current page contains text "email/password format is incorrect."

##### Test case R1.10: If email/password are correct, redirect to /
Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#pasword`
 - click element input `[type="submit"]`
 - get current page's URL and validate it's equal to base_url+'/'

##### Test case R1.11: Otherwise, redict to /login and show message 'email/password combination incorrect'

Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter "test1_frontend@test.com" into element `#email`
 - enter test_user's password into element `#password`
 - click element input `[type="submit"]`
 - get current page's URL and validate it's equal to base_url+'/login'
 - validate current page contains element `#message`
 - validate the text field of `#message` is "email/password combination incorrect"

##### Test case R4.1: The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. - positive

Mocking:
 - Mock backend.get_ticket to return a test_ticket instance
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element input `[type="submit"]`
 - open /
 - enter test_ticket's owner into element `#owner's-email`
 - enter "correctname" into element `#name`
 - enter test_ticket's quantity into element `#quantity`
 - enter test_ticket's price into element `#price`
 - enter test_ticket's date into element `#date`
 - click element input `[type="sell_submit"]`
 - validate current page contains element `#message`
 - validate `#message` shows "successful"
 - open /logout

##### Test case R4.1: The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. - negative

Mocking:
 - Mock backend.get_ticket to return a test_ticket instance
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element input `[type="submit"]`
 - open /
 - enter test_ticket's owner into element `#owner's-email`
 - enter "wrong*name" into element `#name`
 - enter test_ticket's quantity into element `#quantity`
 - enter test_ticket's price into element `#price`
 - enter test_ticket's date into element `#date`
 - click element input `[type="sell_submit"]`
 - validate current page contains element `#message`
 - validate `#message` shows "invalid ticket name"
 - open /
 - enter test_ticket's owner into element `#owner's-email`
 - enter " wrongname" into element `#name`
 - enter test_ticket's quantity into element `#quantity`
 - enter test_ticket's price into element `#price`
 - enter test_ticket's date into element `#date`
 - click element input `[type="sell_submit"]`
 - validate current page contains element `#message`
 - validate `#message` shows "invalid ticket name"
 - open /
 - enter test_ticket's owner into element `#owner's-email`
 - enter "wrongname " into element `#name`
 - enter test_ticket's quantity into element `#quantity`
 - enter test_ticket's price into element `#price`
 - enter test_ticket's date into element `#date`
 - click element input `[type="sell_submit"]`
 - validate current page contains element `#message`
 - validate `#message` shows "invalid ticket name"
 - open /logout (to clean up)

##### Test case R4.2: The name of the ticket is no longer than 60 characters - positive
Mocking:
 - Mock backend.get_ticket to return a test_ticket instance
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element input `[type="submit"]`
 - open /
 - enter test_ticket's owner into element `#owner's-email`
 - enter a string with 59 characters into element `#name`
 - enter test_ticket's quantity into element `#quantity`
 - enter test_ticket's price into element `#price`
 - enter test_ticket's date into element `#date`
 - click element input `[type="sell_submit"]`
 - validate current page contains element `#message`
 - validate `#message` shows "successful"
 - open /logout (to clean up)

##### Test case R4.2: The name of the ticket is no longer than 60 characters - negative
Mocking:
 - Mock backend.get_ticket to return a test_ticket instance
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element input `[type="submit"]`
 - open /
 - enter test_ticket's owner into element `#owner's-email`
 - enter a string with over 60 characters into element `#name`
 - enter test_ticket's quantity into element `#quantity`
 - enter test_ticket's price into element `#price`
 - enter test_ticket's date into element `#date`
 - click element input `[type="sell_submit"]`
 - validate current page contains element `#message`
 - validate `#message` shows "ticket name too long"
 - open /logout (to clean up)

##### Test case R4.3: The quantity of the tickets has to be more than 0, and less than or equal to 100. - positive

Mocking:
 - Mock backend.get_ticket to return a test_ticket instance
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element input `[type="submit"]`
 - open /
 - enter test_ticket's owner into element `#owner's-email`
 - enter test_ticket's name into element `#name`
 - enter "50" into element `#quantity`
 - enter test_ticket's price into element `#price`
 - enter test_ticket's date into element `#date`
 - click element input `[type="sell_submit"]`
 - validate current page contains element `#message`
 - validate `#message` shows "successful"
 - open /logout (to clean up)

##### Test case R4.3: The quantity of the tickets has to be more than 0, and less than or equal to 100. - negative

Mocking:
 - Mock backend.get_ticket to return a test_ticket instance
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element input `[type="submit"]`
 - open /
 - enter test_ticket's owner into element `#owner's-email`
 - enter test_ticket's name into element `#name`
 - enter "0" into element `#quantity`
 - enter test_ticket's price into element `#price`
 - enter test_ticket's date into element `#date`
 - click element input `[type="sell_submit"]`
 - validate current page contains element `#message`
 - validate `#message` shows "ticket quantity out of range"
 - open /
 - enter test_ticket's owner into element `#owner's-email`
 - enter test_ticket's name into element `#name`
 - enter "101" into element `#quantity`
 - enter test_ticket's price into element `#price`
 - enter test_ticket's date into element `#date`
 - validate current page contains element `#message`
 - validate `#message` shows "ticket quantity out of range"
 - open /logout (to clean up)

##### Test case R4.4: Price has to be of range [10, 100] - positive

Mocking:
 - Mock backend.get_ticket to return a test_ticket instance
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element input `[type="submit"]`
 - open /
 - enter test_ticket's owner into element `#owner's-email`
 - enter test_ticket's name into element `#name`
 - enter test_ticket's quantity into element `#quantity`
 - enter "50" into element `#price`
 - enter test_ticket's date into element `#date`
 - click element input `[type="sell_submit"]`
 - validate current page contains element `#message`
 - validate `#message` shows "successful"
 - open /logout (to clean up)

##### Test case R4.4: Price has to be of range [10, 100] - negative

Mocking:
 - Mock backend.get_ticket to return a test_ticket instance
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element input `[type="submit"]`
 - open /
 - enter test_ticket's owner into element `#owner's-email`
 - enter test_ticket's name into element `#name`
 - enter test_ticket's quantity into element `#quantity`
 - enter "9" into element `#price`
 - enter test_ticket's date into element `#date`
 - click element input `[type="sell_submit"]`
 - validate current page contains element `#message`
 - validate `#message` shows "ticket quantity out of range"
 - enter "101" into element `#price`
 - validate current page contains element `#message`
 - validate `#message` shows "ticket quantity out of range"
 - open /logout (to clean up)

##### Test case R4.5: Date must be given in the format YYYYMMDD (e.g. 20200901) - positive

Mocking:
 - Mock backend.get_ticket to return a test_ticket instance
 - Mock backend.get_user to return a test_user instance
 - Mock backend.get_year to return a test_year instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element input `[type="submit"]`
 - open /
 - enter test_ticket's owner into element `#owner's-email`
 - enter test_ticket's name into element `#name`
 - enter test_ticket's quantity into element `#quantity`
 - enter test_ticket's price into element `#price`
 - enter test_year's year+month+day into element `#date`
 - click element input `[type="sell_submit"]`
 - validate current page contains element `#message`
 - validate `#message` shows "successful"
 - open /logout

##### Test case R4.5: Date must be given in the format YYYYMMDD (e.g. 20200901) - negative

Mocking:
 - Mock backend.get_ticket to return a test_ticket instance
 - Mock backend.get_user to return a test_user instance
 - Mock backend.get_year to return a test_year instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element input `[type="submit"]`
 - open /
 - enter test_ticket's owner into element `#owner's-email`
 - enter test_ticket's name into element `#name`
 - enter test_ticket's quantity into element `#quantity`
 - enter test_ticket's price into element `#price`
 - enter test_year's year+month into element `#date`
 - click element input `[type="sell_submit"]`
 - validate current page contains element `#message`
 - validate `#message` shows "date format not valid"
 - enter test_year's month+day into element `#date`
 - validate current page contains element `#message`
 - validate `#message` shows "date format not valid"
 - open /logout (to clean up)

##### Test case R4.6: For any errors, redirect back to / and show an error message
Mocking:
 - Mock backend.get_ticket to return a test_ticket instance
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element input `[type="submit"]`
 - open /
 - enter test_ticket's owner into element `#owner's-email`
 - enter "wrong*name" into element `#name`
 - enter test_ticket's quantity into element `#quantity`
 - enter test_ticket's price into element `#price`
 - enter test_ticket's date into element `#date`
 - click element input `[type="sell_submit"]`
 - validate current page contains element `#message`
 - get current page's url and validate it's equal to base_url + "/"
 - enter test_ticket's owner into element `#owner's-email`
 - enter a string with over 60 characters into element `#name`
 - enter test_ticket's quantity into element `#quantity`
 - enter test_ticket's price into element `#price`
 - enter test_ticket's date into element `#date`
 - click element input `[type="sell_submit"]`
 - validate current page contains element `#message`
 - get current page's url and validate it's equal to base_url + "/"
 - enter test_ticket's owner into element `#owner's-email`
 - enter test_ticket's name into element `#name`
 - enter "0" into element `#quantity`
 - enter test_ticket's price into element `#price`
 - enter test_ticket's date into element `#date`
 - click element input `[type="sell_submit"]`
 - validate current page contains element `#message`
 - get current page's url and validate it's equal to base_url + "/"
 - enter test_ticket's owner into element `#owner's-email`
 - enter test_ticket's name into element `#name`
 - enter test_ticket's quantity into element `#quantity`
 - enter "120" into element `#price`
 - enter test_ticket's date into element `#date`
 - click element input `[type="sell_submit"]`
 - validate current page contains element `#message`
 - get current page's url and validate it's equal to base_url + "/"
 - /logout (to clean up)

##### Test case R4.7: The added new ticket information will be posted on the user profile page

Mocking:
 - Mock backend.get_ticket to return a test_ticket instance
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element input `[type="submit"]`
 - open /
 - enter test_ticket's owner into element `#owner's-email`
 - enter test_ticket's name into element `#name`
 - enter test_ticket's quantity into element `#quantity`
 - enter test_ticket's price into element `#price`
 - enter test_ticket's date into element `#date`
 - click element input `[type="sell_submit"]`
 - open /
 - validate current page contains element `#test_ticket_name`
 - validate the text field of `#test_ticket_name` equals test_user's name
 - open /logout (to clean up)

##### Test Case R7./: Logout will invalid the current session and redirect to the login page. After logout, the user shouldn't be able to access restricted pages.
 
Actions:
 - open /logout
 - validate current page contains element `#login-reminder`
 - open /
 - validate current page contains element `#message`
 - validate that `#message` shows "please login before accessing this page."
 - open /sell
 - validate current page contains element `#message`
 - validate that `#message` shows "please login before accessing this page."
 - open /buy
 - validate current page contains element `#message`
 - validate that `#message` shows "please login before accessing this page."
 - open /update
 - validate current page contains element `#message`
 - validate that `#message` shows "please login before accessing this page."

##### Test Case R8./: For any other requests except the ones above, the system should return a 404 error.

Mocking:
 - Mock backend.get_user to return a test_user instance

Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /*
 - validate current page contains element `#error_404`
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element input `[type="submit"]`
 - validate current page contains element `#welcome-header`
 - open /*
 - validate current page contains element `#error_404`
 - open /logout (to clean up)