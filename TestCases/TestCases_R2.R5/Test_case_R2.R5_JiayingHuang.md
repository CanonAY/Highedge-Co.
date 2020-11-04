Test Data:

```python
test_user = User(
	email = 'test_frontend@test.com',
  name = 'test_frontend',
  password = generate_password_has('test_frontend')
)

test_form = Form(
  email = '', 
  password = ''
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

test_registration = Registration(
  email = 'test_frontend@test.com',
  name = 'test_name',
  password = generate_password_has('test_frontend')
  password1 = password
)
```

##### Test case R2.1: If the user has logged in, redirect back to the user profile page

Mocking:

- Mock backend.get_user to return a test_user instance

Actions:

- Open /logout to invalid any logged-in sessions that may exist
- Open /login
- Enter test_user's email into element ```#email```
- Enter test_user's password into element ```#password```
- Click element `input[type="submit"]`
- Open /register
- Validate that current page's URL is equal to base_url+'/''

##### Test case R2.2: If the user has not logged in, show the user registration page

Actions:

- open /logout
- open /register
- Validate that current page contains element `#[type="submit_registration"]`

##### Test case R2.3: The registration page shows a registration form requesting: email, user name, password, password2

Actions:

- Open /logout
- Open /register
- Validate that current page contains `#email` `#name` `#password` `#password2` elements

##### Test case R2.4: The registration form can be submitted as a POST request to the current URL (/register)

- Mock backend.get_registration to return a test_user instance
- Mock backend.get_form to return a test_form instance

Actions:

- Open /logout to invalid any logged-in sessions may exist
- Open /register
- Enter test_registration's email into element `#email`
- Enter test_registration's name into element `#name`
- Enter test_registration's password into element `#password`
- Enter test_registration's password2 into element `#password2`
- Click element input `[type="submit"]`
- Validate that the value of `test_form.email` is identical to the text field of `#email`
- Validate that the value of `test_form.name` is identical to the text field of `#name`
- Validate that the value of `test_form.password` is identical to the text field of `#password`
- Validate that the value of `test_form.password2` is identical to the text field of `#password2`

##### Test case R2.5: Email, password, password2 all have to satisfy the same required as defined in R1 - positive

Mocking:

 - Mock backend.get_registration to return a test_user instance
- Mock backend.get_email to return a test_email instance

Actions:

 - Open /logout (to invalid any logged-in sessions may exist)
 - Open /register
 - Enter test_registration's email into element `#email`
- Enter test_registration's name into element `#name`
- Enter test_registration's password into element `#password`
- Enter test_registration's password2 into element `#password2`
- Click element input `[type="submit"]`
 - Validate that current page shows "successful" in `#message` element

##### Test case R2.5: Email, password, password2 all have to satisfy the same required as defined in R1 - negative

Mocking:

 - Mock backend.get_registration to return a test_user instance
- Mock backend.get_email to return a test_email instance

Actions:

 - Open /logout (to invalid any logged-in sessions may exist)
 - Open /register
 - Enter test_registration's name into element `#name`
- Enter test_registration's password into element `#password`
- Enter test_registration's password2 into element `#password2`
- Click element input `[type="submit"]`
 - Validate that current page shows "failed -- email and password cannot be empty" in `#message` element
 - Open /register
 - Enter test_email's local_part into element `#email`
- Enter test_registration's name into element `#name`
- Enter test_registration's password into element `#password`
- Enter test_registration's password2 into element `#password2`
- Click element input `[type="submit"]`
 - Validate that current page shows "failed -- email has to follow addr-spec defined in RFC 5322" in `#message` element
 - Open /register
 - Enter test_registration's email into element `#email`
- Enter test_registration's name into element `#name`
- Enter "123aB*" into element `#password` and `#password2`
- Click element input `[type="submit"]`
 - Validate that current page shows "failed -- password must meet complexity requirement" in `#message` element
 - Enter "123ab*" into element `#password` and `#password2`
- Click element input `[type="submit"]`
 - Validate that current page shows "failed -- password must meet complexity requirement" in `#message` element
 - Enter "123BC*" into element `#password` and `#password2`
- Click element input `[type="submit"]`
 - Validate that current page shows "failed -- password must meet complexity requirement" in `#message` element
 - Enter "123abc" into element `#password` and `#password2`
- Click element input `[type="submit"]`
 - Validate that current page shows "failed -- password must meet complexity requirement" in `#message` element

##### Test case R2.6: Password and password2 have to be exactly the same - positive

Mocking:

- Mock backend.get_registration to return a test_user instance
- Mock backend.get_form to return a test_form instance

Actions:

- Open /logout
- Open /register
- Enter test_registration's email into element `#email`
- Enter test_registration's name into element `#name`
- Enter "testpassword1" into element `#password`
- Enter "testpassword1" into element `#password2`
- Click element input `[type="submit"]`
- Validate that current page shows "successful" in `#message` element

##### Test case R2.6: Password and password2 have to be exactly the same - negative

Mocking:

- Mock backend.get_registration to return a test_user instance
- Mock backend.get_form to return a test_form instance

Actions:

- Open /logout
- Open /register
- Enter test_registration's email into element `#email`
- Enter test_registration's name into element `#name`
- Enter "testpassword1" into element `#password`
- Enter "differentpassword" into element `#password2`
- Click element input `[type="submit"]`
- Validate that current page shows "fail" in `#message` element

##### Test case R2.7: User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character - positive

Mocking:

- Mock backend.get_registration to return a test_user instance

Actions:

- Open /logout to invalid any logged-in sessions may exist
- Open /register
- Enter test_registration's email into element `#email`
- Enter test_registration's name into element `#name`
- Enter test_registration's password into element `#password`
- Enter test_registration's password2 into element `#password2`
- Click element input `[type="submit"]`
- Validate that current page shows "successful" in `#message` element

##### Test case R2.7: User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character - negative

Mocking:

- Mock backend.get_registration to return a test_user instance

Actions:

- Open /logout to invalid any logged-in sessions may exist
- Open /register
- Enter test_registration's email into element `#email`
- Enter “” _(an empty name)_ into element `#name`
- Enter test_registration's password into element `#password`
- Enter test_registration's password2 into element `#password2`
- Click element input `[type="submit"]`
- Validate that current page shows "fail" in `#message` element
- Open /register
- Enter test_registration's email into element `#email`
- Enter “not-alphanumeric-only” into element `#name`
- Enter test_registration's password into element `#password`
- Enter test_registration's password2 into element `#password2`
- Click element input `[type="submit"]`
- Validate that current page shows "fail" in `#message` element
- Enter test_registration's email into element `#email`
- Enter " namewithspace " into element `#name`
- Enter test_registration's password into element `#password`
- Enter test_registration's password2 into element `#password2`
- Click element input `[type="submit"]`
- Validate that current page shows "fail" in `#message` element

##### Test case R2.8: User name has to be longer than 2 characters and less than 20 characters - positive

Mocking:

- Mock backend.get_registration to return a test_user instance

Actions:

- Open /logout to invalid any logged-in sessions may exist
- Open /register
- Enter test_registration's email into element `#email`
- Enter "aProperName" into element `#name`
- Enter test_registration's password into element `#password`
- Enter test_registration's password2 into element `#password2`
- Click element input `[type="submit"]`
- Validate that current page shows "successful" in `#message` element

##### Test case R2.8: User name has to be longer than 2 characters and less than 20 characters - negative

Mocking:

- Mock backend.get_registration to return a test_user instance

Actions:

- Open /logout to invalid any logged-in sessions may exist
- Open /register
- Enter test_registration's email into element `#email`
- Enter "tt" into element `#name`
- Enter test_registration's password into element `#password`
- Enter test_registration's password2 into element `#password2`
- Click element input `[type="submit"]`
- Validate that current page shows "fail" in `#message` element
- Open /register
- Enter test_registration's email into element `#email`
- Enter "longerThanTwentyChars" into element `#name`
- Enter test_registration's password into element `#password`
- Enter test_registration's password2 into element `#password2`
- Click element input `[type="submit"]`
- Validate that current page shows "fail" in `#message` element

##### Test case R2.9: For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute)

Mocking:

- Mock backend.get_registration to return a test_registration instance

Actions:

- Open /logout to invalid any logged-in sessions may exist
- Open /registration
- Enter 'test@' into element `#email`
- Enter test_registration's name into element `#name`
- Enter test_registration's password into element `#password`

- Enter test_registration's password2 into element `#password2`
- Click element `#[type="registration_submit"]
- Validate that current page's URL is equal to base_url+'/login'
- Validate that current page contains `#message` element
- Validate that the parameter of format() of element `#message` is 'email invalid'
- Open /registration

##### Test case R2.10: If the email already exists, show message 'this email has been ALREADY used'

Mocking:

- Mock backend.get_registration to return a test_registraion instance

Actions:

- Open /logout to invalid any logged-in sessions may exist
- Open /registration
- Enter test_registraion's email into element `#email`
- Enter test_registration's name into element `#name`
- Enter test_registration's password into element `#password`

- Enter test_registration's password2 into element `#password2`
- Click element `#[type="registration_submit"]`
- Validate that current page's URL is equal to base_url+'/login'
- Validate that current page contains "successful" in `#message` element
- Open /registraion
- Enter test_registraion's email into element `#email`
- Enter test_registration's name into element `#name`
- Enter test_registration's password into element `#password`

- Enter test_registration's password2 into element `#password2`
- Click element `#[type="registration_submit"]`
- Validate that the current page shows "this email has been ALREADY used" in `#message` element

##### Test case R2.11: If no error regarding the inputs following the reules above, create a new user, set the balance to 5000, and go back to the /login page

Mocking:

- Mock backend.get_registration to return a test_registraion instance

Actions:

- Open /logout to invalid any logged-in sessions may exist
- Open /registration
- Enter test_registraion's email into element `#email`
- Enter test_registration's name into element `#name`
- Enter test_registration's password into element `#password`

- Enter test_registration's password2 into element `#password2`
- Click element `#[type="registration_submit"]`
- Validate that current page's URL is equal to base_url+'/login'
- Validate that current page contains "successful" in `#message` element
- Open /login
- Enter test_registration's email into element `#email`
- Enter test_registration's password into element `#password`
- Click element input `[type="submit"]`
- Validate that the balance equals to "5000"
- Open /logout

##### Test case R5.1: The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character - positive

Mocking:

- Mock backend.get_ticket to return a test_ticket instance
- Mock backend.get_user to return a test_user instance

Action:

- Open /logout to invalid any logged-in sessions may exist
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element input `[type="submit"]`
- Open /
- Enter test_ticket's owner into element `#owner's-email`
- Enter "testname" into element `#name`
- Enter test_ticket's quantity into element `#quantity`
- Enter test_ticket's price into element `#price`
- Enter test_ticket's date into element `#date`
- Click element input `[type="sell_submit"]`
- Validate current page contains element `#message`
- Validate `#message` shows "successful"
- Enter test_ticket's name into element `#name`
- Click element input `[type="update_submit"]`
- Validate current page contains element `#message`
- Validate `#message` shows "successful"
- Open /logout

##### Test case R5.1: The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character - negative

Mocking:

- Mock backend.get_ticket to return a test_ticket instance
- Mock backend.get_user to return a test_user instance

Actions:

- Open /logout

- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element input `[type="submit"]`
- Open /
- Enter test_ticket's owner into element `#owner's-email`
- Enter test_ticket's name into element `#name`
- Enter test_ticket's quantity into element `#quantity`
- Enter test_ticket's price into element `#price`
- Enter test_ticket's date into element `#date`
- Click element input `[type="sell_submit"]`
- Validate current page shows "successful" in element `#message`
- Enter "not-alphanumeric-only" into element `#name`
- Click element input `[type="update_submit"]`
- Validate `#message` shows "invalid ticket name"
- Enter " namewithspace " into element `#name`
- click element input `[type="update_submit"]`
- Validate current page contains element `#message`
- Validate `#message` shows "invalid ticket name"
- Open /logout

##### Test case R5.2: The name of the ticket is no longer than 60 characters - positive 

Mocking:

- Mock backend.get_ticket to return a test_ticket instance
- Mock backend.get_user to return a test_user instance

Actions:

- Open /logout to invalid any logged-in sessions may exist
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element input `[type="submit"]`
- Open /
- Enter test_ticket's owner into element `#owner's-email`
- Enter test_ticket's name into element `#name`
- Enter test_ticket's quantity into element `#quantity`
- Enter test_ticket's price into element `#price`
- Enter test_ticket's date into element `#date`
- Click element input `[type="sell_submit"]`
- Validate current page contains element `#message`
- Validate `#message` shows "successful"
- Enter test_ticket's name into element `#name`
- Click element input `[type="update_submit"]`
- Validate current page contains element `#message`
- Validate `#message` shows "successful"
- Open /logout

##### Test case R5.2: The name of the ticket is no longer than 60 characters - negative 

Mocking:

- Mock backend.get_ticket to return a test_ticket instance
- Mock backend.get_user to return a test_user instance

Actions:

- Open /logout to invalid any logged-in sessions may exist
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element input `[type="submit"]`
- Open /
- Enter test_ticket's owner into element `#owner's-email`
- Enter test_ticket's name into element `#name`
- Enter test_ticket's quantity into element `#quantity`
- Enter test_ticket's price into element `#price`
- Enter test_ticket's data into element `#date`
- Click element input `[type="sell_submit"]`
- Validate current page contains element `#message`
- Validate `#message` shows "successful"
- Enter a string with ___61 characters___ into element `#name`
- Click element input `[type="update_submit"]`
- Validate that page shows "ticket name too long" in element `#message`
- Open /logout

##### Test case R5.3: The quantity of the tickets has to be more than 0, and less than or equal to 100 - positive

Mocking:

- Mock backend.get_ticket to return a test_ticket instance
- Mock backend.get_user to return a test_user instance

Actions:

- Open /logout to invalid any logged-in sessions may exist
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element input `[type="submit"]`
- Open /
- Enter test_ticket's owner into element `#owner's-email`
- Enter test_ticket's name into element `#name`
- Enter test_quantity into element `#quantity`
- Enter test_ticket's price into element `#price`
- Enter test_ticket's date into element `#date`
- Click element input `[type="sell_submit"]`
- Validate current page contains element `#message`
- Validate `#message` shows "successful"
- Enter "50" into element `#quantity`
- Click element input `[type="update_submit"]`
- Validate that the page shows "successful" in element `#message`
- Open /logout

##### Test case R5.3: The quantity of the tickets has to be more than 0, and less than or equal to 100 - negative

Mocking:

- Mock backend.get_ticket to return a test_ticket instance
- Mock backend.get_user to return a test_user instance

Actions:

- Open /logout to invalid any logged-in sessions may exist
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element input `[type="submit"]`
- Open /
- Enter test_ticket's owner into element `#owner's-email`
- Enter test_ticket's name into element `#name`
- Enter test_ticket's quantity into element `#quantity`
- Enter test_ticket's price into element `#price`
- Enter test_ticket's date into element `#date`
- Click element input `[type="sell_submit"]`
- Validate current page contains element `#message`
- Validate `#message` shows "successful"
- Enter "0" into element `#quantity`
- Click element input `[type="update_submit"]`
- Validate `#message` shows "ticket quantity out of range"
- Open /
- Enter "101" into element `#quantity`
- Click element input `[type="update_submit"]`
- Validate current page contains element `#message`
- Validate `#message` shows "ticket quantity out of range"
- Open /logout

##### Test case R5.4: Price has to be of range [10, 100] - positive

Mocking:

- Mock backend.get_ticket to return a test_ticket instance
- Mock backend.get_user to return a test_user instance

Actions:

- Open /logout to invalid any logged-in sessions may exist
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element input `[type="submit"]`
- Open /
- Enter test_ticket's owner into element `#owner's-email`
- Enter test_ticket's name into element `#name`
- Enter test_ticket's quantity into element `#quantity`
- Enter test_ticket's price into element `#price`
- Enter test_ticket's date into element `#date`
- Click element input `[type="sell_submit"]`
- Validate current page contains element `#message`
- Validate `#message` shows "successful"
- Enter "50" into element `#price`
- Click element input `[type="update_submit"]`
- Validate that page shows "successful" in element `#message`
- Open /logout

##### Test case R5.4: Price has to be of range [10, 100] - negative

Mocking:

- Mock backend.get_ticket to return a test_ticket instance
- Mock backend.get_user to return a test_user instance

Actions:

- Open /logout to invalid any logged-in sessions may exist
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element input `[type="submit"]`
- Open /
- Enter test_ticket's owner into element `#owner's-email`
- Enter test_ticket's name into element `#name`
- Enter test_ticket's quantity into element `#quantity`
- Enter test_ticket's price into element `#price`
- Enter test_ticket's date into element `#date`
- Click element input `[type="sell_submit"]`
- Validate current page contains element `#message`
- Validate `#message` shows "successful"
- Enter "9" into element `#price`
- Click element input `[type="update_submit"]`
- Validate that page shows "ticket price out of range" in element `#message`
- Enter "101" into element `#price`
- Click element input `[type="update_submit"]`
- Validate current page contains element `#message`
- Validate `#message` shows "ticket price out of range"
- Open /logout

##### Test case R5.5: Date must be given in the format YYYYMMDD - positive

Mocking:

- Mock backend.get_ticket to return a test_ticket instance
- Mock backend.get_user to return a test_user instance
- Mock backend.get_year to return a test_year instance

Actions:

- Open /logout to invalid any logged-in sessions may exist
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element input `[type="submit"]`
- Open /
- Enter test_ticket's owner into element `#owner's-email`
- Enter test_ticket's name into element `#name`
- Enter test_ticket's quantity into element `#quantity`
- Enter test_ticket's price into element `#price`
- Enter test_ticket's date into element `#date`
- Click element input `[type="sell_submit"]`
- Validate current page contains element `#message`
- Validate `#message` shows "successful"
- Enter test_year's year+month+day into element `#date`
- Click element input `[type="update_submit"]`
- Validate current page contains element `#message`
- Validate `#message` shows "successful"
- Open /logout

##### Test case R5.5: Date must be given in the format YYYYMMDD - negative

Mocking:

- Mock backend.get_ticket to return a test_ticket instance
- Mock backend.get_user to return a test_user instance
- Mock backend.get_year to return a test_year instance

Actions:

- Open /logout to invalid any logged-in sessions may exist
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element input `[type="submit"]`
- Open /
- Enter test_ticket's owner into element `#owner's-email`
- Enter test_ticket's name into element `#name`
- Enter test_ticket's quantity into element `#quantity`
- Enter test_ticket's price into element `#price`
- Enter test_ticket's date into element `#date`
- Click element input `[type="sell_submit"]`
- Validate current page contains element `#message`
- Validate `#message` shows "successful"
- Enter test_year's ***year+month*** into element `#date`
- Click element input `[type="update_submit"]`
- Validate current page contains element `#message`
- Validate `#message` shows "date format not valid"
- Enter test_year's ***month+day*** into element `#date`
- Click element input `[type="update_submit"]`
- Validate current page contains element `#message`
- Validate `#message` shows "date format not valid"
- Open /logout

##### Test case R5.6: The ticket of the given name must exist - positive

Mocking:

- Mock backend.get_ticket to return a test_ticket instance
- Mock backend.get_user to return a test_user instance

Actions:

- Open /logout to invalid any logged-in sessions may exist
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element input `[type="submit"]`
- Open /
- Enter test_ticket's owner into element `#owner's-email`
- Enter test_ticket's name into element `#name`
- Enter test_ticket's quantity into element `#quantity`
- Enter test_ticket's price into element `#price`
- Enter test_ticket's date into element `#date`
- Click element input `[type="sell_submit"]`
- Validate current page contains element `#message`
- Validate `#message` shows "successful"
- Enter test_ticket's name into element `#name`
- Click element input `[type="update_submit"]`
- Validate current page contains element `#message`
- Validate `#message` shows "successful"
- Open /logout

##### Test case R5.6: The ticket of the given name must exist - negative

Mocking:

- Mock backend.get_ticket to return a test_ticket instance
- Mock backend.get_user to return a test_user instance

Actions:

- Open /logout to invalid any logged-in sessions may exist
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element input `[type="submit"]`
- Open /
- Enter test_ticket's name into element `#name`
- Click element input `[type="update_submit"]`
- Validate that page shows "fail" in element `#message`
- Open /logout

##### Test case R5.7: For any errors, redirect back to / and show an error message

Mocking:

 - Mock backend.get_ticket to return a test_ticket instance
 - Mock backend.get_user to return a test_user instance

Actions:

 - Open /logout to invalid any logged-in sessions may exist
 - Open /login
 - Enter test_user's email into element `#email`
 - Enter test_user's password into element `#password`
 - Click element input `[type="submit"]`
 - Open /
 - Enter test_ticket's owner into element `#owner's-email`
- Enter test_ticket's name into element `#name`
- Enter test_ticket's quantity into element `#quantity`
- Enter test_ticket's price into element `#price`
- Enter test_ticket's date into element `#date`
- Click element input `[type="sell_submit"]`
- Validate current page contains element `#message`
- Validate `#message` shows "successful"
 - Enter "wrong*name" into element `#name`
 - Click element input `[type="update_submit"]`
 - Validate current page contains element `#message`
 - Get current page's url and validate it's equal to base_url + "/"
 - Enter a string with over 60 characters into element `#name`
 - Click element input `[type="update_submit"]`
 - Validate current page contains element `#message`
 - Get current page's url and validate it's equal to base_url + "/"
 - Enter "0" into element `#quantity`
 - Click element input `[type="update_submit"]`
 - Validate current page contains element `#message`
 - Get current page's url and validate it's equal to base_url + "/"
 - Enter "120" into element `#price`
 - Click element input `[type="update_submit"]`
 - Validate current page contains element `#message`
 - Get current page's url and validate it's equal to base_url + "/"
 - Open /logout