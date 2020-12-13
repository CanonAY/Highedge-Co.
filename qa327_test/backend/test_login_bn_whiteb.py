import pytest
from qa327.models import db, User
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from qa327.backend import login_user, get_user

class WhiteBoxLoginTest(BaseCase):

    def register(self):
        """add new user to database for the purpose of testing"""
        self.open(base_url + '/register')
        self.type("#email", "whitebox@test.com")
        self.type("#name", "whitebox")
        self.type("#password", "WHITE_box")
        self.type("#password2", "WHITE_box")
        self.click('input[type="submit"]')
        self.assert_title('Log In')

    def test_login_user(self, *_):
        self.register()
        user = get_user("whitebox@test.com")

        """ T1: (not user): True; (not check_password_hash(user.password, password)): True; (not email == user.email): True """
        assert login_user("boxwhite", "white_BOX") == None

        """ T2: (not user): False;(not check_password_hash(user.password, password)): True; (not email == user.email): True """
        assert login_user("whitebox", "white_BOX") == None

        """ T3: (not user): True; (not check_password_hash(user.password, password)): False;(not email == user.email): True """
        assert login_user("boxwhite", "WHITE_box") == None

        """ T4: (not user): True; (not check_password_hash(user.password, password)): True; (not email == user.email): False"""
        assert login_user("boxwhite@test.com", "white_BOX") == None

        """ T5: (not user): False;(not check_password_hash(user.password, password)): False;(not email == user.email): True """
        assert login_user("whitebox", "WHITE_box") == None

        """ T6: (not user): True; (not check_password_hash(user.password, password)): False;(not email == user.email): False"""
        assert login_user("boxwhite@test.com", "WHITE_box") == None

        """ T7: (not user): False;(not check_password_hash(user.password, password)): True; (not email == user.email): False"""
        assert login_user("whitebox@test.com", "white_BOX") == None

        """ T8: (not user): False;(not check_password_hash(user.password, password)): False;(not email == user.email): False"""
        assert login_user("whitebox@test.com", "WHITE_box") == user


