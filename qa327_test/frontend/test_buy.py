import pytest
from seleniumbase import BaseCase
from selenium.webdriver.common.keys import Keys

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Ticket 
from werkzeug.security import generate_password_hash, check_password_hash

"""
This test_buy file defines all unit tests for the frontend buy page.
"""

#Mock the sample user 
test_user =User(
	  email = 'test_buy@test.com',
	  name = 'test_buy',
      balance = 5000,
	  password = generate_password_hash('TEST_frontend'),
)

class FrontEndR6Test(BaseCase):

    def login(self):
        """
        Before starting each test case, we need to test whether we can loggin sucessfully
        """
        #make sure to log out before testing
        self.open(base_url + '/logout')
        #use the sample user to loggin 
        self.open(base_url + '/login')
        self.type("#email", "test_buy@test.com")
        self.type("#password", "TEST_frontend")
        self.click('input[type="submit"]')

    def sell_input(self):
        """
        This add new ticket that has the name TESTticket1 with quantity 50 into the database
        """
        self.type("#sell-name", "testTicket1")
        self.type("#sell-quantity", "50")
        self.type("#sell-price", "50")
        date = self.find_element("#sell-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Submit Selling Ticket"]')
        #return to profile page 
        self.open(base_url)
        """
        This add new ticket that has the name TESTticket1 with quantity 50 into the database
        """
        self.type("#sell-name", "TESTticket3")
        self.type("#sell-quantity", "60")
        self.type("#sell-price", "90")
        date = self.find_element("#sell-date")
        date.send_keys("2021", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"25")
        self.click('input[value="Submit Selling Ticket"]')
        #return to profile page 
        self.open(base_url)


    @patch('qa327.backend.get_user', return_value=test_user)
    def test_name_format(self,*_):
        """
        Test Case: R6.1
        Test that name has to be alphanumeric-only, 
        and spaced are not allowed in the first or last character
        """
        #login to the profile
        self.login()
        self.sell_input()

        """
        Negative: enter invalid ticekt name
        """
        # negative1: first characater is space 
        self.type("#buy-name", " BUYticket123")
        self.type("#buy-quantity", "40")
        self.click('input[value="Submit Buying Ticket"]')
        # assert ticket submit failed
        self.assert_element("#message_b")
        self.assert_text("Ticket format invalid", "#message_b")
        self.open(base_url)

        # negative2: last characater is space 
        self.type("#buy-name", "BUYticket123 ")
        self.type("#buy-quantity", "40")
        self.click('input[value="Submit Buying Ticket"]')
        # assert ticket submit failed
        self.assert_element("#message_b")
        self.assert_text("Ticket format invalid", "#message_b")
        self.open(base_url)
        """
        Positive: enter valid ticket name
        """
        self.type("#buy-name", "testTicket1")
        self.type("#buy-quantity", "40")
        self.click('input[value="Submit Buying Ticket"]')
        # assert ticket submit succeed 
        self.assert_element("#message")
        self.assert_text("Transaction successful", "#message")
        # return to the profil page 
        self.open(base_url)

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_name_length(self,*_):
        """
        Test Case: R6.2
        Test that ticket name is no longer than 60 characteres.
        """
        #login to the profile
        self.login()
        self.sell_input()
        #negative: ticket name has the length that is more than 60 characters
        self.type("#buy-name", "TESTticket1TESTticket1TESTticket1TESTticket1TESTticket1TESTticket1TESTticket1") 
        self.type("#buy-quantity", "4")
        self.click('input[value="Submit Buying Ticket"]')
        self.assert_element("#message_b")
        self.assert_text("Ticket format invalid", "#message_b")
        self.open(base_url)

        #postive: ticket name has thee length that is less than 60 characters
        self.type("#buy-name", "testTicket1") 
        self.type("#buy-quantity", "4")
        self.click('input[value="Submit Buying Ticket"]')
        self.assert_element("#message")
        self.assert_text("Transaction successful", "#message")
        self.open(base_url)


    @patch('qa327.backend.get_user', return_value=test_user)
    def test_quantity(self,*_):
        """
        Test Case: R6.3
        Test that the quantity of the ticket is <=100, ans >0
        """
        #login to the profile
        self.login()
        self.sell_input()
        #negative: ticket quantithy is more than 100
        self.type("#buy-name", "testTicket1") 
        self.type("#buy-quantity", "104")
        self.click('input[value="Submit Buying Ticket"]')
        self.assert_element("#message_b")
        self.assert_text("Ticket format invalid", "#message_b")
        self.open(base_url)
        #positive: ticket quantity is between 0 and 100(inclusive)
        self.type("#buy-name", "testTicket1") 
        self.type("#buy-quantity", "40")
        self.click('input[value="Submit Buying Ticket"]')
        self.assert_element("#message")
        self.assert_text("Transaction successful", "#message")
        self.open(base_url)

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_exist_enough(self,*_):
        """
        Test Case: R6.4
        Test that the ticket exist in the database
        and the request quantity is more than enough 
        """
        #login to the profile
        self.login()
        self.sell_input()

        #negative1: ticket does not exist
        self.type("#buy-name", "testTicket2") 
        self.type("#buy-quantity", "40")
        self.click('input[value="Submit Buying Ticket"]')
        self.assert_element("#message_b")
        self.assert_text("Ticket format invalid", "#message_b")
        self.open(base_url)
        
        #negative2: ticket does exist but doesn't have enough quantity 
        self.type("#buy-name", "testTicket1") 
        self.type("#buy-quantity", "60")
        self.click('input[value="Submit Buying Ticket"]')
        self.assert_element("#message_b")
        self.assert_text("Ticket format invalid", "#message_b")
        self.open(base_url)

        #positive: ticket exist and ticket has enough quantity 
        self.type("#buy-name", "testTicket1") 
        self.type("#buy-quantity", "20")
        self.click('input[value="Submit Buying Ticket"]')
        self.assert_element("#message")
        self.assert_text("Transaction successful", "#message")
        self.open(base_url)

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_balance(self,*_):
        """
        Test Case: R6.5
        Test that user has enough balance to pay the required ticekt price
        """
        #login to the profile
        self.login()
        self.sell_input()

        #negative: user didn't have enough balance to buy the ticket
        self.type("#buy-name", "TESTticket3") 
        self.type("#buy-quantity", "45")
        self.click('input[value="Submit Buying Ticket"]')
        self.assert_element("#message_b")
        self.assert_text("Ticket format invalid", "#message_b")
        self.open(base_url)

        #positive: user has enough balance to buy the ticket
        self.type("#buy-name", "testTicket1") 
        self.type("#buy-quantity", "30")
        self.click('input[value="Submit Buying Ticket"]')
        self.assert_element("#message")
        self.assert_text("Transaction successful", "#message")
        self.open(base_url)

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_redirect(self,*_):
        """
        Test Case: R6.6
        Test that if any errors, redirect to / and show error message
        """
        #login to the profile
        self.login()
        self.sell_input()

        #negative1: enter invalid ticket name with invalid character
        self.type("#buy-name", "testTicket1_") 
        self.type("#buy-quantity", "45")
        self.click('input[value="Submit Buying Ticket"]')
        self.assert_element("#message_b")
        self.assert_text("Ticket format invalid", "#message_b")
        self.open(base_url)
        #negative2: enter invalid ticket name with invalid length
        self.type("#buy-name", 7*"testTicket1") 
        self.type("#buy-quantity", "45")
        self.click('input[value="Submit Buying Ticket"]')
        self.assert_element("#message_b")
        self.assert_text("Ticket format invalid", "#message_b")
        self.open(base_url)
        #negative3: enter valid ticket name and invalid ticket quantity
        self.type("#buy-name", "testTicket1") 
        self.type("#buy-quantity", "-1")
        self.click('input[value="Submit Buying Ticket"]')
        self.assert_element("#message_b")
        self.assert_text("Ticket format invalid", "#message_b")
        self.open(base_url)
        #negative4: enter valid ticket name and unavailable quantity
        self.type("#buy-name", "testTicket1") 
        self.type("#buy-quantity", "60")
        self.click('input[value="Submit Buying Ticket"]')
        self.assert_element("#message_b")
        self.assert_text("Ticket format invalid", "#message_b")
        self.open(base_url)
        #negative5: enter valid ticket name with the quantity that the user's balance won't meet the requirement
        self.type("#buy-name", "TESTticket3") 
        self.type("#buy-quantity", "50")
        self.click('input[value="Submit Buying Ticket"]')
        self.assert_element("#message_b")
        self.assert_text("Ticket format invalid", "#message_b")
        self.open(base_url)