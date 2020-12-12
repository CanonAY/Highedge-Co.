import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all unit tests for the frontend login page.
"""

# Moch a sample user
test_user1 = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('TEST_frontend')
)

class FrontEndLoginTest(BaseCase):

    # R1.1: If the user hasn't logged in, show the login page
    def test_not_loggedin(self, *_):
        # invalidate any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        # confirm title of the page is "Log In"
        self.assert_title("Log In")

    # R1.2: the login page has a message that by default says 'please login'
    def test_please_login(self, *_):
        # invalid any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        # confirm there is a message says "Please login"
        self.assert_element("#message")
        self.assert_text("Please login", "#message")
          
    # R1.3: If the user has logged in, redirect to the user profile page
    @patch('qa327.backend.get_user', return_value=test_user1)
    def test_redirect_to_profile(self, *_):
        # invalid any existing session
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

    # R1.4: The login page provides a login form which requests two fields: email and passwords
    def test_login_form(self, *_):
        # invalidate any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        # confirm current page contains a form that requests email and password
        self.assert_element("#email")
        self.assert_element("#password")

    # R1.5: The login form can be submitted as a POST request to the current URL (/login)
    def test_post(self, *_):
        # invalidate any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        # confirm current page contains a POST request element
        self.assert_element('form[method="post"]')

    # R1.6: Email and password both cannot be empty
    @patch('qa327.backend.get_user', return_value=test_user1)
    def test_form_cant_empty(self, *_):
        # invalid any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/login')

        """ NEGATIVE """
        # enter test user email
        self.type("#email", "test_frontend@test.com")
        # click enter button
        self.click('input[type="submit"]')
        # confirm login to profile failed
        self.assert_title("Log In")

        self.open(base_url + '/login')

        # enter test user password
        self.type("#password", "TEST_frontend")
        # click enter button
        self.click('input[type="submit"]')
        # confirm login to profile failed
        self.assert_title("Log In")
   
        self.open(base_url + '/login')

        """ POSITIVE """
        # enter test user email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "TEST_frontend")
        # click enter button
        self.click('input[type="submit"]')
        # confirm currently on profile page
        self.assert_title("Profile")
        self.open(base_url + '/logout')

    # R1.7: Email has to follow addr-spec defined in RFC 5322
    @patch('qa327.backend.get_user', return_value=test_user1)
    def test_email_format(self, *_):
        # invalid any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/login')

        """ NEGATIVE """
        # enter wrong email and correct password
        self.type("#email", "testfrontend")
        self.type("#password", "TEST_frontend")
        # click enter button
        self.click('input[type="submit"]')
        # confirm login to profile failed
        self.assert_title("Log In")

        self.open(base_url + '/login')

        """ POSITIVE """
        # enter test user email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "TEST_frontend")
        # click enter button
        self.click('input[type="submit"]')
        # confirm currently on profile page
        self.assert_title("Profile")
        self.open(base_url + '/logout')

    # R1.8: Password has to meet the required complexity: minimum length 6, 
    # at least one upper case, at least one lower case, and at least 
    # one  special character
    @patch('qa327.backend.get_user', return_value=test_user1)
    def test_password_complexity(self, *_):
        # invalid any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/login')

        """ NEGATIVE """
        # enter correct email and wrong password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "testfrontend")
        # click enter button
        self.click('input[type="submit"]')
        # confirm login to profile failed
        self.assert_title("Log In")

        self.open(base_url + '/login')

        """ POSITIVE """
        # enter test user email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "TEST_frontend")
        # click enter button
        self.click('input[type="submit"]')
        # confirm currently on profile page
        self.assert_title("Profile")
        self.open(base_url + '/logout')

    # R1.9: For any formatting errors, render the login page and show the message  
    # 'email/password format is incorrect.'
    @patch('qa327.backend.get_user', return_value=test_user1)
    def test_format_incorrect(self, *_):
        # invalid any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/login')

        """ NEGATIVE """
        # enter correct email and wrong password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "testfrontend")
        # click enter button
        self.click('input[type="submit"]')
        # confirm login to profile failed, correct error message shown  
        self.assert_element("#message")
        self.assert_text("email/password format is incorrect.", "#message")

        self.open(base_url + '/login')

        # enter wrong email and correct password
        self.type("#email", "testfrontend")
        self.type("#password", "TEST_frontend")
        # click enter button
        self.click('input[type="submit"]')
        # confirm login to profile failed, correct error message shown  
        self.assert_element("#message")
        self.assert_text("email/password format is incorrect.", "#message")

        self.open(base_url + '/login')

        """ POSITIVE """
        # enter test user email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "TEST_frontend")
        # click enter button
        self.click('input[type="submit"]')
        # confirm currently on profile page
        self.assert_title("Profile")
        self.open(base_url + '/logout')

    # R1.10: If email/password are correct, redirect to /
    @patch('qa327.backend.get_user', return_value=test_user1)
    def test_login_success(self, *_):
        # invalid any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        # enter test user email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "TEST_frontend")
        # click enter button
        self.click('input[type="submit"]')
        # confirm currently on profile page
        self.assert_title("Profile")
        self.open(base_url + '/logout')

    # R1.11: Otherwise, redirect to /login and show message  'email/password combination incorrect'
    @patch('qa327.backend.get_user', return_value=test_user1)
    def test_login_failed(self, *_):
        # invalid any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        # enter test user email and password
        self.type("#email", "frontend_test@test.com")
        self.type("#password", "TEST_frontend")
        # click enter button
        self.click('input[type="submit"]')
        # confirm currently on profile page
        self.assert_element("#message")
        self.assert_text("email/password combination incorrect", "#message")
