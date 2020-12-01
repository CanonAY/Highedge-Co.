import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all unit tests for the frontend homepage.

The tests will only test the frontend portion of the program, by patching the backend to return
specfic values. For example:

@patch('qa327.backend.get_user', return_value=test_user)

Will patch the backend get_user function (within the scope of the current test case)
so that it return 'test_user' instance below rather than reading
the user from the database.

Annotate @patch before unit tests can mock backend methods (for that testing function)
"""

# Moch a sample user
test_user = User(
    email='test_frontend@test.com',
    name='testFrontend',
    password=generate_password_hash('TEST_frontend')
)

# Moch some sample tickets
test_tickets = [
    {'name': 't1', 'price': '100'}
]

class FrontEndRegistrationTest(BaseCase):
    
    # R2.1: If the user has logged in, redirect back to the user profile page
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_loggedin(self, *_):
        # invalidate any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        # enter test user email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "TEST_frontend")
        # click enter button
        self.click('input[type="submit"]')
        self.open(base_url + '/login')
        # confirm currently on profile page
        self.assert_title("Profile")
        
    # R2.2: If the user has not logged in, show the user registration page
    def test_not_loggedin(self, *_):
        # invalidate any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        # confirm title of the page is "registration"
        self.assert_title("Register")
        
    # R2.3: The registration page shows a registration form requesting:
    # email, user name, password, password2
    def test_registration_form(self, *_):
        # invalidate any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        # confirm current page contains a form that requests:
        # email, user name, password, password2
        self.assert_element("#email")
        self.assert_element("#name")
        self.assert_element("#password")
        self.assert_element("#password2")
        
    # R2.4: The registration form can be submitted as a POST
    # request to the current URL (/register)
    def test_POST_request(self, *_):
        # invalidate any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        # confirm current page contains a POST request element
        self.assert_element('form[method="post"]')
        
    # R2.5: Email, password, password2 all have to satisfy
    # the same required as defined in R1
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_email_password_complexity_positive(self, *_):
        
        # 1) ----- Email and password cannot be empty -----
        
        # invalidate any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        
        # enter test user name, email, and password
        self.type("#name", "testFrontend")
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "TEST_frontend")
        self.type("#password2", "TEST_frontend")
        
        # click enter button
        self.click('input[type="submit"]')
        # confirm register succeed
        self.assert_text_not_visible("#message")
        
        # 2) ----- Email has to follow addr-spec defined in RFC 5322 -----
        
        # invalidate any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        
        # enter email that follows addr-spec defined in RFC 5322
        # user name and password also in correct format
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "testFrontend")
        self.type("#password", "TEST_frontend")
        self.type("#password2", "TEST_frontend")
        
        # click enter button
        self.click('input[type="submit"]')
        # confirm register succeed
        self.assert_text_not_visible("#message")
        
        # 3) ----- Password must meet complexity requirement -----
        
        # invalidate any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        
        # enter passwords that meet the complexity requirement
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "testFrontend")
        self.type("#password", "TEST_frontend")
        self.type("#password2", "TEST_frontend")
        
        # click enter button
        self.click('input[type="submit"]')
        # confirm register succeed
        self.assert_text_not_visible("#message")
        
    # R2.5: Email, password, password2 all have to satisfy
    # the same required as defined in R1
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_email_password_complexity_negative(self, *_):
        
        # 1) ----- Email and password cannot be empty -----
        
        # invalidate any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        
        # enter only test user name email, no password
        self.type("#name", "testFrontend")
        self.type("#email", "test_frontend@test.com")
        # click enter button
        self.click('input[type="submit"]')
        # confirm register failed
        assert "Please login" not in "#message"
        
        # invalidate any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        
        # enter only test user name and password, no email
        self.type("#name", "testFrontend")
        self.type("#password", "TEST_frontend")
        self.type("#password2", "TEST_frontend")
        # click enter button
        self.click('input[type="submit"]')
        # confirm login to profile failed
        assert "Please login" not in "#message"
        
        # 2) ----- Email has to follow addr-spec defined in RFC 5322 -----
        
        # invalidate any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        
        # enter wrong email and correct user name and password
        self.type("#email", "testfrontend")     # incorrect format
        self.type("#name", "testFrontend")
        self.type("#password", "TEST_frontend")
        self.type("#password2", "TEST_frontend")
        
        # click enter button
        self.click('input[type="submit"]')
        # confirm register failed
        assert "Please login" not in "#message"
        
        # 3) ----- Password must meet complexity requirement -----
        
        # invalidate any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        
        # enter correct email and user name, but wrong password
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "testFrontend")
        self.type("#password", "testfrontend")  # incorrect format
        self.type("#password2", "testfrontend")  # incorrect format
        
        # click enter button
        self.click('input[type="submit"]')
        # confirm register failed
        assert "Please login" not in "#message"
        
    # R2.6: Password and password2 have to be exactly the same
    def test_password_same_positive(self, *_):
        
        # invalidate any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        
        # password and password2 are identical
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "testFrontend")
        self.type("#password", "TEST_frontend")
        self.type("#password2", "TEST_frontend")
        
        # click enter button
        self.click('input[type="submit"]')
        # confirm register succeed
        self.assert_text_not_visible("#message")
        
    # R2.6: Password and password2 have to be exactly the same
    def test_password_same_negative(self, *_):
        
        # invalidate any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        
        # password and password2 are identical
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "testFrontend")
        self.type("#password", "TEST_frontend")
        self.type("#password2", "Another_password")
        
        # click enter button
        self.click('input[type="submit"]')
        # confirm register failed
        assert "Please login" not in "#message"
        
    # R2.7: User name has to be non-empty, alphanumeric-only, 
    # and space allowed only if it is not the first or the last character
    def test_username_format_positive(self, *_):
        
        # invalidate any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        
        # user name in correct format
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "testFrontend")
        self.type("#password", "TEST_frontend")
        self.type("#password2", "TEST_frontend")
        
        # click enter button
        self.click('input[type="submit"]')
        # confirm register succeed
        self.assert_text_not_visible("#message")
        
        
    # R2.7: User name has to be non-empty, alphanumeric-only, 
    # and space allowed only if it is not the first or the last character
    def test_username_format_negative(self, *_):
        
        # invalidate any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        
        # 1) ----- user name is empty -----
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "")
        self.type("#password", "TEST_frontend")
        self.type("#password2", "TEST_frontend")
        
        # click enter button
        self.click('input[type="submit"]')
        # confirm register failed
        assert "Please login" not in "#message"
        
        # 2) ----- user name is not alphanumeric -----
        self.open(base_url + '/register')
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "abc!!defg")
        self.type("#password", "TEST_frontend")
        self.type("#password2", "TEST_frontend")
        
        # click enter button
        self.click('input[type="submit"]')
        # confirm register failed
        assert "Please login" not in "#message"
        
        # 3) ----- space in first and last character -----
        self.open(base_url + '/register')
        self.type("#email", "test_frontend@test.com")
        self.type("#name", " testFrontend ")
        self.type("#password", "TEST_frontend")
        self.type("#password2", "TEST_frontend")
        
        # click enter button
        self.click('input[type="submit"]')
        # confirm register failed
        assert "Please login" not in "#message"
        
    # R2.8: User name has to be longer than 2 characters and less than 20 characters
    def test_username_length_positive(self, *_):
        
        # invalidate any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        
        # user name in correct length
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "testFrontend")
        self.type("#password", "TEST_frontend")
        self.type("#password2", "TEST_frontend")
        
        # click enter button
        self.click('input[type="submit"]')
        # confirm register succeed
        self.assert_text_not_visible("#message")
        
    # R2.8: User name has to be longer than 2 characters and less than 20 characters
    def test_username_length_negative(self, *_):
        
        # invalidate any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
    
        # 1) ----- user name less than 2 characters -----
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "t")
        self.type("#password", "TEST_frontend")
        self.type("#password2", "TEST_frontend")
    
        # click enter button
        self.click('input[type="submit"]')
        # confirm register failed
        assert "Please login" not in "#message"
        
        # 2) ----- user name longer than 20 characters -----
        self.open(base_url + '/register')
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "testFrontendAbcdEfghijklmn")
        self.type("#password", "TEST_frontend")
        self.type("#password2", "TEST_frontend")
        
        # click enter button
        self.click('input[type="submit"]')
        # confirm register failed
        assert "Please login" not in "#message"
        
    # R2.9: For any formatting errors, redirect back to /login and show message
    # '{} format is incorrect.'.format(the_corresponding_attribute)
    def test_formatting_error(self, *_):
        
        # invalidate any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        
        # 1) ----- user name has formatting errors -----
        self.type("#email", "test_frontend@test.com")
        self.type("#name", " incorrect_format! ")
        self.type("#password", "TEST_frontend")
        self.type("#password2", "TEST_frontend")
        
        # click enter button
        self.click('input[type="submit"]')
        # confirm register failed and redirect back to /login
        assert "Please login" not in "#message"
        # confirm the page shows message
        # '{} format is incorrect.'.format(the_corresponding_attribute)
        self.assert_text("User name format is incorrect", "#message")
        
        # invalidate any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        
        # 2) ----- user email has formatting errors -----
        self.type("#email", "test_frontend")
        self.type("#name", "testFrontend")
        self.type("#password", "TEST_frontend")
        self.type("#password2", "TEST_frontend")
        
        # click enter button
        self.click('input[type="submit"]')
        # confirm register failed and redirect back to /login
        assert "Please login" not in "#message"
        # confirm the page shows message
        # '{} format is incorrect.'.format(the_corresponding_attribute)
        self.assert_text("Email format is incorrect", "#message")
        
        # invalidate any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        
        # 2) ----- password has formatting errors -----
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "testFrontend")
        self.type("#password", "testfrontend")
        self.type("#password2", "testfrontend")
        
        # click enter button
        self.click('input[type="submit"]')
        # confirm register failed and redirect back to /login
        assert "Please login" not in "#message"
        # confirm the page shows message
        # '{} format is incorrect.'.format(the_corresponding_attribute)
        self.assert_text("Password format is incorrect", "#message")
        
    # R2.10: If the email already exists, show message
    # 'this email has been ALREADY used'
    def test_email_exist(self, *_):
        
        # invalidate any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        
        # register successfully
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "testFrontend")
        self.type("#password", "TEST_frontend")
        self.type("#password2", "TEST_frontend")
        
        # click enter button
        self.click('input[type="submit"]')
        # confirm register succeed
        self.assert_text_not_visible("#message")
        
        # invalidate any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        
        # register again with same user information
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "testFrontend")
        self.type("#password", "TEST_frontend")
        self.type("#password2", "TEST_frontend")
        
        # click enter button
        self.click('input[type="submit"]')
        # confirm register failed
        self.assert_text("this email has been ALREADY used", "#message")
        
    # R2.11: If no error regarding the inputs following the reules above,
    # create a new user, set the balance to 5000, and go back to the /login page
    def no_error(self, *_):
        
        # invalidate any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/register')
        
        # register successfully
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "testFrontend")
        self.type("#password", "TEST_frontend")
        self.type("#password2", "TEST_frontend")
        
        # click enter button
        self.click('input[type="submit"]')
        # confirm register succeed
        self.assert_text_not_visible("#message")
        
        # login with information above
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "TEST_frontend")
        self.click('input[type="submit"]')
        
        # validate that the balance equals to "5000"
        self.assert_text("5000","#balance")
        
        # log out
        self.open(base_url + '/logout')