import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all unit tests for the backend method login_user().
"""

class BackEndLoginTest(BaseCase):

    
    # This method uses input partition testing approach
    def test_login_user(self, *_):
        # invalidate any existing session
        self.open(base_url + '/logout')
        # open register page
        self.open(base_url + '/register')

        # enter test user email, name and password
        self.type("#email", "test_bn_frontend@test.com")
        self.type("#name", "testfrontend")
        self.type("#password", "TEST_frontend")
        self.type("#password2", "TEST_frontend")
        # click submit button
        self.click('input[type="submit"]')
        # confirm registration succeed, currently on login page
        self.assert_title("Log In")
                
        """ test 1: user exists in database, password matches the email, email inserted is exact same as what stored in database """
        self.type("#email", "test_bn_frontend@test.com")
        self.type("#password", "TEST_frontend")
        self.click('input[type="submit"]')
        # confirm login success, session granted
        self.assert_title("Profile")

        self.open(base_url + '/logout')

        """ test 2: user does not exist in database, password matches the email, email inserted is exact same as what stored in database """
        self.type("#email", "frontend_test@test.com")
        self.type("#password", "TEST_frontend")
        self.click('input[type="submit"]')
        # confirm login failed
        self.assert_title("Log In")

        """ test 3: user exists in database, password doesn't match the email, email inserted is exact same as what stored in database """
        self.type("#email", "test_bn_frontend@test.com")
        self.type("#password", "frontend_TEST")
        self.click('input[type="submit"]')
        # confirm login failed
        self.assert_title("Log In")

        """ test 4: user exists in database, password matches the email, email inserted is not same as what stored in database """
        self.type("#email", "test_bn_frontend")
        self.type("#password", "frontend_TEST")
        self.click('input[type="submit"]')
        # confirm login failed
        self.assert_title("Log In")

        """ test 5: user does not exist in database, password doesn't match the email, email inserted is exact same as what stored in database """
        self.type("#email", "frontend_test@test.com")
        self.type("#password", "frontend_TEST")
        self.click('input[type="submit"]')
        # confirm login failed
        self.assert_title("Log In")

        """ test 6: user exists in database, password doesn't match the email, email inserted is not same as what stored in database """
        self.type("#email", "test_frontend")
        self.type("#password", "frontend_TEST")
        self.click('input[type="submit"]')
        # confirm login failed
        self.assert_title("Log In")

        """ test 7: user does not exist in database, password matches the email, email inserted is not same as what stored in database """
        self.type("#email", "frontend_test")
        self.type("#password", "frontend_TEST")
        self.click('input[type="submit"]')
        # confirm login failed
        self.assert_title("Log In")