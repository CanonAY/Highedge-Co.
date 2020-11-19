import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines the unit test that tests program behavior when user logout from current session.
"""

# Moch a sample user
test_user2 = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('TEST_frontend')
)

class FrontEndLogoutTest(BaseCase):

    # R7: Logout will invalid the current session and redirect to the login page.
    # After logout, the user shouldn't be able to access restricted pages.
    @patch('qa327.backend.get_user', return_value=test_user2)
    def test_logout(self, *_):
        # invalid any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        # enter test user email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "TEST_frontend")
        # click enter button
        self.click('input[type="submit"]')

        # logout from current session
        self.open(base_url + '/logout')
        # confirm redirected to log in page
        self.assert_title("Log In")

        # attempt to access user profile
        self.open(base_url + '/')
        # confirm attempt failed
        self.assert_title("Log In")