import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines the unit test that tests program behavior when user try to access a page that is not exist.
"""

class FrontEnd404Test(BaseCase):

    # For any other requests except the ones above, the system should return a 404 error
    def test_open_wrong_page(self, *_):
        # Open a page which do not exist
        self.open(base_url + '/error')
        # Check currently on 404 page
        self.assert_title("404 Not Found")