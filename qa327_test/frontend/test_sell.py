import pytest
from seleniumbase import BaseCase
from selenium.webdriver.common.keys import Keys

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all unit tests for the frontend login page.
"""

# Moch a sample user
test_user = User(
    email='test_sell@test.com',
    name='test_sell',
    password=generate_password_hash('TEST_frontend')
)

class FrontEndSellTest(BaseCase):

    # Login to the profile for the purpose of testing functionality of sell form. 
    def login_to_profile(self):
        # invalid any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        # enter test user email and password
        self.type("#email", "test_sell@test.com")
        self.type("#password", "TEST_frontend")
        # click enter button
        self.click('input[type="submit"]')

    # R4.1 The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_name_format(self, *_):
        # login to the profile
        self.login_to_profile()

        """ NEGATIVE """
        # enter invalid name and valid quantity, price and date
        self.type("#sell-name", " TESTticket")
        self.type("#sell-quantity", "50")
        self.type("#sell-price", "50")
        date = self.find_element("#sell-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT, "31")
        self.click('input[value="Submit Selling Ticket"]')
        # assert ticket submit failed
        self.assert_element("#message_s")
        self.assert_text("Ticket format invalid", "#message_s")

        self.open(base_url)

        # enter invalid name and valid quantity, price and date
        self.type("#sell-name", "TESTticket ")
        self.type("#sell-quantity", "50")
        self.type("#sell-price", "50")
        date = self.find_element("#sell-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Submit Selling Ticket"]')
        # assert ticket submit failed
        self.assert_element("#message_s")
        self.assert_text("Ticket format invalid", "#message_s")

        self.open(base_url)

        # enter invalid name and valid quantity, price and date
        self.type("#sell-name", "TE_STticket")
        self.type("#sell-quantity", "50")
        self.type("#sell-price", "50")
        date = self.find_element("#sell-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Submit Selling Ticket"]')
        # assert ticket submit failed
        self.assert_element("#message_s")
        self.assert_text("Ticket format invalid", "#message_s")

        self.open(base_url)

        """ POSITIVE """
        # enter valid name, quantity, price and date
        self.type("#sell-name", "TESTticket")
        self.type("#sell-quantity", "50")
        self.type("#sell-price", "50")
        date = self.find_element("#sell-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Submit Selling Ticket"]')
        # assert ticket submit succeed
        self.assert_element("#message")
        self.assert_text("Ticket successfully posted", "#message")

        self.open(base_url)

    # R4.2 The name of the ticket is no longer than 60 characters
    # R4.8 (optional) The name of the tickets has to contain at least 6 characters
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_name_length(self, *_):
        # login to the profile
        self.login_to_profile()

        """ NEGATIVE """
        # enter invalid name and valid quantity, price and date
        self.type("#sell-name", 6*"TESTticket1")
        self.type("#sell-quantity", "50")
        self.type("#sell-price", "50")
        date = self.find_element("#sell-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Submit Selling Ticket"]')
        # assert ticket submit failed
        self.assert_element("#message_s")
        self.assert_text("Ticket format invalid", "#message_s")

        self.open(base_url)

        # enter invalid name and valid quantity, price and date
        self.type("#sell-name", "TEST1")
        self.type("#sell-quantity", "50")
        self.type("#sell-price", "50")
        date = self.find_element("#sell-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Submit Selling Ticket"]')
        # assert ticket submit failed
        self.assert_element("#message_s")
        self.assert_text("Ticket format invalid", "#message_s")

        self.open(base_url)

        """ POSITIVE """
        # enter valid name, quantity, price and date
        self.type("#sell-name", "TESTticket1")
        self.type("#sell-quantity", "50")
        self.type("#sell-price", "50")
        date = self.find_element("#sell-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Submit Selling Ticket"]')
        # assert ticket submit succeed
        self.assert_element("#message")
        self.assert_text("Ticket successfully posted", "#message")

        self.open(base_url)

    # R4.3 The quantity of the tickets has to be more than 0, and less than or equal to 100.
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_quantity(self, *_):
        # login to the profile
        self.login_to_profile()

        """ NEGATIVE """
        # enter invalid quantity and valid name, price and date
        self.type("#sell-name", "TESTticket2")
        self.type("#sell-quantity", "0")
        self.type("#sell-price", "50")
        date = self.find_element("#sell-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Submit Selling Ticket"]')
        # assert ticket submit failed
        self.assert_element("#message_s")
        self.assert_text("Ticket format invalid", "#message_s")

        self.open(base_url)

        # enter invalid quantity and valid name, price and date
        self.type("#sell-name", "TESTticket2")
        self.type("#sell-quantity", "102")
        self.type("#sell-price", "50")
        date = self.find_element("#sell-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Submit Selling Ticket"]')
        # assert ticket submit failed
        self.assert_element("#message_s")
        self.assert_text("Ticket format invalid", "#message_s")

        self.open(base_url)

        """ POSITIVE """
        # enter valid name, quantity, price and date
        self.type("#sell-name", "TESTticket2")
        self.type("#sell-quantity", "50")
        self.type("#sell-price", "50")
        date = self.find_element("#sell-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Submit Selling Ticket"]')
        # assert ticket submit succeed
        self.assert_element("#message")
        self.assert_text("Ticket successfully posted", "#message")

        self.open(base_url)

    # R4.4 Price has to be of range [10, 100]
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_price(self, *_):
        # login to the profile
        self.login_to_profile()

        """ NEGATIVE """
        # enter invalid price and valid name, quantity and date
        self.type("#sell-name", "TESTticket3")
        self.type("#sell-quantity", "50")
        self.type("#sell-price", "0")
        date = self.find_element("#sell-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Submit Selling Ticket"]')
        # assert ticket submit failed
        self.assert_element("#message_s")
        self.assert_text("Ticket format invalid", "#message_s")

        self.open(base_url)

        # enter invalid price and valid name, quantity and date
        self.type("#sell-name", "TESTticket3")
        self.type("#sell-quantity", "50")
        self.type("#sell-price", "102")
        date = self.find_element("#sell-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Submit Selling Ticket"]')
        # assert ticket submit failed
        self.assert_element("#message_s")
        self.assert_text("Ticket format invalid", "#message_s")

        self.open(base_url)

        """ POSITIVE """
        # enter valid name, quantity, price and date
        self.type("#sell-name", "TESTticket3")
        self.type("#sell-quantity", "50")
        self.type("#sell-price", "50")
        date = self.find_element("#sell-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Submit Selling Ticket"]')
        # assert ticket submit succeed
        self.assert_element("#message")
        self.assert_text("Ticket successfully posted", "#message")

        self.open(base_url)

    # R4.5 Date must be given in the format YYYYMMDD (e.g. 20200901)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_date(self, *_):
        # login to the profile
        self.login_to_profile()

        """ NEGATIVE """
        # enter invalid date and valid name, price and quantity
        self.type("#sell-name", "TESTticket4")
        self.type("#sell-quantity", "50")
        self.type("#sell-price", "50")
        date = self.find_element("#sell-date")
        date.send_keys("201202", "12", "31")
        self.click('input[value="Submit Selling Ticket"]')
        # assert ticket submit failed
        self.assert_element("#message_s")
        self.assert_text("Ticket format invalid", "#message_s")

        self.open(base_url)

        """ POSITIVE """
        # enter valid name, quantity, price and date
        self.type("#sell-name", "TESTticket4")
        self.type("#sell-quantity", "50")
        self.type("#sell-price", "50")
        date = self.find_element("#sell-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Submit Selling Ticket"]')
        # assert ticket submit succeed
        self.assert_element("#message")
        self.assert_text("Ticket successfully posted", "#message")

        self.open(base_url)

    # R4.6 For any errors, redirect back to / and show an error message
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_redirect(self, *_):
        # login to the profile
        self.login_to_profile()

        # enter invalid name and valid date, price and quantity
        self.type("#sell-name", "TEST_ticket5")
        self.type("#sell-quantity", "50")
        self.type("#sell-price", "50")
        date = self.find_element("#sell-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Submit Selling Ticket"]')
        # assert ticket submit failed
        self.assert_title("Profile")
        self.assert_element("#message_s")
        self.assert_text("Ticket format invalid", "#message_s")

        self.open(base_url)

        # enter invalid quantity and valid date, price and name
        self.type("#sell-name", "TEST_ticket5")
        self.type("#sell-quantity", "0")
        self.type("#sell-price", "50")
        date = self.find_element("#sell-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Submit Selling Ticket"]')
        # assert ticket submit failed
        self.assert_title("Profile")
        self.assert_element("#message_s")
        self.assert_text("Ticket format invalid", "#message_s")

        self.open(base_url)

        # enter invalid price and valid name, quantity and date
        self.type("#sell-name", "TESTticket5")
        self.type("#sell-quantity", "50")
        self.type("#sell-price", "0")
        date = self.find_element("#sell-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Submit Selling Ticket"]')
        # assert ticket submit failed
        self.assert_title("Profile")
        self.assert_element("#message_s")
        self.assert_text("Ticket format invalid", "#message_s")

        self.open(base_url)

        # enter invalid date and valid name, price and quantity
        self.type("#sell-name", "TESTticket5")
        self.type("#sell-quantity", "50")
        self.type("#sell-price", "50")
        date = self.find_element("#sell-date")
        date.send_keys("201202", "12", "31")
        self.click('input[value="Submit Selling Ticket"]')
        # assert ticket submit failed
        self.assert_title("Profile")
        self.assert_element("#message_s")
        self.assert_text("Ticket format invalid", "#message_s")

        self.open(base_url)

    # R4.7 The added new ticket information will be posted on the user profile page
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_post_ticket(self, *_):
        # login to the profile
        self.login_to_profile()

        # enter valid name, quantity, price and date
        self.type("#sell-name", "TESTticket6")
        self.type("#sell-quantity", "50")
        self.type("#sell-price", "50")
        date = self.find_element("#sell-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Submit Selling Ticket"]')
        # assert ticket submit succeed
        self.assert_element("#message")
        self.assert_text("Ticket successfully posted", "#message")

        self.open(base_url)

        # assert the ticket posted on profile page
        self.assert_text("TESTticket6")
