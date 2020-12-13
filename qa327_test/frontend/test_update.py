import pytest
from seleniumbase import BaseCase
from selenium.webdriver.common.keys import Keys

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash


# Moch a sample user
test_user = User(
    email='test_frontend@test.com',
    name='testFrontend',
    password=generate_password_hash('TEST_frontend')
)

class FrontEndUpdatingTest(BaseCase):
    
    # Login to the profile for the purpose of testing functionality of sell form. 
    def login_to_profile(self):
        # invalid any existing session
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        # enter test user email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "TEST_frontend")
        # click enter button
        self.click('input[type="submit"]')
        
    # Create an initial ticket, and try to update this ticket
    def first_sell_ticket(self):
        # enter valid name, quantity, price and date
        self.type("#sell-name", "TESTupdate")
        self.type("#sell-quantity", "50")
        self.type("#sell-price", "50")
        date = self.find_element("#sell-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Submit Selling Ticket"]')

    # R5.1: The name of the ticket has to be alphanumeric-only,
    # and space allowed only if it is not the first or the last character
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_ticketName(self, *_):
        
        # login to the profile
        self.login_to_profile()
        # first sell a ticket
        self.first_sell_ticket()
        
        self.open(base_url + '/')
        
        """ NEGATIVE """
        # enter invalid test_ticket's name and valid quantity, price, date
        self.type("#update-name", " TESTupdate")
        self.type("#update-quantity", "50")
        self.type("#update-price", "50")
        date = self.find_element("#update-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT, "31")
        self.click('input[value="Update Selling Ticket"]')
        # assert ticket submit failed
        self.assert_element("#message_u")
        self.assert_text("Ticket format invalid", "#message_u")
        
        self.open(base_url + '/')
        
        # enter invalid name and valid quantity, price and date
        self.type("#update-name", "TESTupdate ")
        self.type("#update-quantity", "50")
        self.type("#update-price", "50")
        date = self.find_element("#update-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Update Selling Ticket"]')
        # assert ticket submit failed
        self.assert_element("#message_u")
        self.assert_text("Ticket format invalid", "#message_u")
        self.open(base_url)
    
        # enter invalid name and valid quantity, price and date
        self.type("#update-name", "TE_STupdate")
        self.type("#update-quantity", "50")
        self.type("#update-price", "50")
        date = self.find_element("#update-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        
        self.click('input[value="Update Selling Ticket"]')
        # assert ticket submit failed
        self.assert_element("#message_u")
        self.assert_text("Ticket format invalid", "#message_u") 
        
        self.open(base_url)
        
        """ POSITIVE """
        # enter valid name, quantity, price and date
        self.type("#update-name", "TESTupdate")
        self.type("#update-quantity", "50")
        self.type("#update-price", "50")
        date = self.find_element("#update-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Update Selling Ticket"]')
        # assert ticket update succeed
        self.assert_element("#message_u")
        self.assert_text("Ticket information updated", "#message_u")
        
        self.open(base_url)
        
        
    # R5.2: The name of the ticket is no longer than 60 characters
    # The name of the tickets has to contain at least 6 characters
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_name_length(self, *_):
        # login to the profile
        self.login_to_profile()
        # first sell a ticket and try to update it
        self.first_sell_ticket()
    
        self.open(base_url)
        
        """ NEGATIVE """
        # enter invalid name and valid quantity, price and date
        self.type("#update-name", 6*"TESTupdate1")
        self.type("#update-quantity", "50")
        self.type("#update-price", "50")
        date = self.find_element("#update-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Update Selling Ticket"]')
        # assert ticket submit failed
        self.assert_element("#message_u")
        self.assert_text("Ticket format invalid", "#message_u")
            
        self.open(base_url)
            
        # enter invalid name and valid quantity, price and date
        self.type("#update-name", "TEST1")
        self.type("#update-quantity", "50")
        self.type("#update-price", "50")
        date = self.find_element("#update-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Update Selling Ticket"]')
        # assert ticket submit failed
        self.assert_element("#message_u")
        self.assert_text("Ticket format invalid", "#message_u")
            
        self.open(base_url)
            
        """ POSITIVE """
        # enter valid name, quantity, price and date
        self.type("#update-name", "TESTupdate")
        self.type("#update-quantity", "50")
        self.type("#update-price", "50")
        date = self.find_element("#update-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Update Selling Ticket"]')
        # assert ticket update succeed
        self.assert_element("#message_u")
        self.assert_text("Ticket information updated", "#message_u")
        
        self.open(base_url)
            
    # R5.3: The quantity of the tickets has to be more than 0, and less than or equal to 100.
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_quantity(self, *_):
        # login to the profile
        self.login_to_profile()
        # first sell a ticket and try to update it
        self.first_sell_ticket()
            
        self.open(base_url)

        """ NEGATIVE """
        # enter invalid quantity and valid name, price and date
        self.type("#update-name", "TESTupdate2")
        self.type("#update-quantity", "0")
        self.type("#update-price", "50")
        date = self.find_element("#update-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Update Selling Ticket"]')
        # assert ticket submit failed
        self.assert_element("#message_u")
        self.assert_text("Ticket format invalid", "#message_u")
            
        self.open(base_url)
            
        # enter invalid quantity and valid name, price and date
        self.type("#update-name", "TESTupdate2")
        self.type("#update-quantity", "102")
        self.type("#update-price", "50")
        date = self.find_element("#update-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Update Selling Ticket"]')
        # assert ticket submit failed
        self.assert_element("#message_u")
        self.assert_text("Ticket format invalid", "#message_u")
    
        self.open(base_url)
            
        """ POSITIVE """
        # enter valid name, quantity, price and date
        self.type("#update-name", "TESTupdate")
        self.type("#update-quantity", "50")
        self.type("#update-price", "50")
        date = self.find_element("#update-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Update Selling Ticket"]')
        # assert ticket update succeed
        self.assert_element("#message_u")
        self.assert_text("Ticket information updated", "#message_u")
        
        self.open(base_url)
            
    # R5.4: Price has to be of range [10, 100]
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_price(self, *_):
        # login to the profile
        self.login_to_profile()
            
        self.open(base_url)

        """ NEGATIVE """
        # enter invalid price and valid name, quantity and date
        self.type("#update-name", "TESTupdate3")
        self.type("#update-quantity", "50")
        self.type("#update-price", "0")
        date = self.find_element("#update-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Update Selling Ticket"]')
        # assert ticket submit failed
        self.assert_element("#message_u")
        self.assert_text("Ticket format invalid", "#message_u")
            
        self.open(base_url)
            
        # enter invalid price and valid name, quantity and date
        self.type("#update-name", "TESTupdate3")
        self.type("#update-quantity", "50")
        self.type("#update-price", "102")
        date = self.find_element("#update-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Update Selling Ticket"]')
        # assert ticket submit failed
        self.assert_element("#message_u")
        self.assert_text("Ticket format invalid", "#message_u")
            
        self.open(base_url)
            
        """ POSITIVE """
        # enter valid name, quantity, price and date
        self.type("#update-name", "TESTupdate")
        self.type("#update-quantity", "50")
        self.type("#update-price", "50")
        date = self.find_element("#update-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Update Selling Ticket"]')
        # assert ticket update succeed
        self.assert_element("#message_u")
        self.assert_text("Ticket information updated", "#message_u")
        
        self.open(base_url)
            
    # R5.5: Date must be given in the format YYYYMMDD (e.g. 20200901)
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_date(self, *_):
        # login to the profile
        self.login_to_profile()
        # first sell a ticket and try to update it
        self.first_sell_ticket()
            
        self.open(base_url)

        """ NEGATIVE """
        # enter invalid date and valid name, price and quantity
        self.type("#update-name", "TESTupdate4")
        self.type("#update-quantity", "50")
        self.type("#update-price", "50")
        date = self.find_element("#update-date")
        date.send_keys("201202", "12", "31")
        self.click('input[value="Update Selling Ticket"]')
        # assert ticket submit failed
        self.assert_element("#message_u")
        self.assert_text("Ticket format invalid", "#message_u")
            
        self.open(base_url)
            
        """ POSITIVE """
        # enter valid name, quantity, price and date
        self.type("#update-name", "TESTupdate")
        self.type("#update-quantity", "50")
        self.type("#update-price", "50")
        date = self.find_element("#update-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Update Selling Ticket"]')
        # assert ticket update succeed
        self.assert_element("#message_u")
        self.assert_text("Ticket information updated", "#message_u")
        
        self.open(base_url)
            
    # R5.6: The ticket of the given name must exist
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_ticket_exist(self, *_):
        # login to the profile
        self.login_to_profile()
        # sell the ticket first
        self.first_sell_ticket()
        
        self.open(base_url)

        """ NEGATIVE """
        # enter valid ticket name that does NOT exist
        self.type("#update-name", "TESTupdate5")
        self.type("#update-quantity", "50")
        self.type("#update-price", "50")
        date = self.find_element("#update-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Update Selling Ticket"]')
        # assert ticket submit failed
        self.assert_title("Profile")
        self.assert_element("#message_u")
        self.assert_text("Ticket format invalid", "#message_u")
        
        """ POSITIVE """
        # enter valid name, quantity, price and date
        self.type("#update-name", "TESTupdate")
        self.type("#update-quantity", "50")
        self.type("#update-price", "50")
        date = self.find_element("#update-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Update Selling Ticket"]')
        # assert ticket update succeed
        self.assert_element("#message_u")
        self.assert_text("Ticket information updated", "#message_u")
        
        self.open(base_url)
        
    
    # R5.7: For any errors, redirect back to / and show an error message
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_redirect(self, *_):
        # login to the profile
        self.login_to_profile()
        # first sell a ticket and try to update it
        self.first_sell_ticket()
        
        self.open(base_url)

        # enter invalid name and valid date, price and quantity
        self.type("#update-name", "TEST_update6")
        self.type("#update-quantity", "50")
        self.type("#update-price", "50")
        date = self.find_element("#update-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
            
        self.click('input[value="Update Selling Ticket"]')
        # assert ticket submit failed
        self.assert_title("Profile")
        self.assert_element("#message_u")
        self.assert_text("Ticket format invalid", "#message_u")
            
        self.open(base_url)
        
        # enter invalid quantity and valid date, price and name
        self.type("#update-name", "TEST_update6")
        self.type("#update-quantity", "0")
        self.type("#update-price", "50")
        date = self.find_element("#update-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Update Selling Ticket"]')
        # assert ticket submit failed
        self.assert_title("Profile")
        self.assert_element("#message_u")
        self.assert_text("Ticket format invalid", "#message_u")
            
        self.open(base_url)
        
        # enter invalid price and valid name, quantity and date
        self.type("#update-name", "TESTupdate6")
        self.type("#update-quantity", "50")
        self.type("#update-price", "0")
        date = self.find_element("#update-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT,"31")
        self.click('input[value="Update Selling Ticket"]')
        # assert ticket submit failed
        self.assert_title("Profile")
        self.assert_element("#message_u")
        self.assert_text("Ticket format invalid", "#message_u")
            
        self.open(base_url)
                
        # enter invalid date and valid name, price and quantity
        self.type("#update-name", "TESTupdate6")
        self.type("#update-quantity", "50")
        self.type("#update-price", "50")
        date = self.find_element("#update-date")
        date.send_keys("201202", "12", "31")
        self.click('input[value="Update Selling Ticket"]')
        # assert ticket submit failed
        self.assert_title("Profile")
        self.assert_element("#message_u")
        self.assert_text("Ticket format invalid", "#message_u")
        