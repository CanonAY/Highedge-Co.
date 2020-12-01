import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Ticket 
from werkzeug.security import generate_password_hash, check_password_hash
"""
Created by: Ziyu Yang 

This is the test case for R3
"""
#Mock the sample user 
test_user =User(
	  email = 'test_frontend@test.com',
	  name = 'test_frontend',
	  password = generate_password_hash('test_frontend'),
	  balance =5000
)

class FrontEndR3Test(BaseCase):

    def login(self):
        """
        Before starting each test case, we need to test whether we can loggin sucessfully
        """
        #make sure to log out before testing
        self.open(base_url + '/logout')
        #use the sample user to loggin 
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_frontend")
        self.click('input[type="submit"]')

    def test_redirect(self, *__):
        """
        Test Case: R3.1
        This is a sample front end unit test the user not loggin 
        and redirect to login page
        """
        #the user has logged out
        self.open(base_url + '/logout')
        #go to the profile page 
        self.open(base_url + '/')
        #check whether the current page is in loggin page 
        self.assert_title("Log In")
        #clean up 
        self.open(base_url + '/logout')

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_show_welcome_header(self, *__):
        """
        Test Case: R3.2
        This is the unit test case that test there is 
        a "Hi [user.name]" welcome header when a sample user login 
        """
        #login by using the mock user
        self.login()
        self.open(base_url + '/')
        #this tests whether there is a header element here
        self.assert_element("#welcome-header")
        #test whether the text fits to what we want 
        self.assert_text("Hi test_frontend", "#welcome-header")
        self.open(base_url + '/logout')

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_show_balance(self, *__):
        """
        Test Case: R3.3
        This tests whether profile page contains user's balance
        """
        #login by using the mock user
        self.login()
        self.open(base_url + '/')
        #after sucessfully loggin, test whether balance shows in the profile page 
        self.assert_element("#balance")
        #test whether the text fits to what we want 
        self.assert_text("Your Balance: 5000", "#balance")
        self.open(base_url + '/logout')

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_show_logout_link(self, *__):
        """
        Test Case: R3.4
        This test case tests a loggout link and point to /logout page
        """
        #login by using the mock user
        self.login()
        self.open(base_url + '/')
        #after sucessfully loggin, test whether logout link pointing to /logout
        self.click_link_text("logout") 
        #verify that we are in the log in page 
        self.assert_title("Log In")

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_list_available_tickets(self, *__):
        """
        Test Case: R3.5
        This test case tests the page shows all available tickets 
        whether it includes all the information of tickets: quantity, owner's email, price
        """
        #login by using the mock user
        self.login()
        self.open(base_url + '/')
        self.assert_text("Ticket Name")
        #test whether it include available ticket name field 
        #self.assert_element("#ticket-name")
        self.assert_text("Ticket Price")
        #test whether it include available ticket price field 
        #self.assert_element("#ticket-price")
        self.assert_text("Ticket Quantity")
        #test whether it include available ticket quantity field 
        #self.assert_element("#ticket-quantity")
        self.assert_text("Owner's Email")
        #test whether it include available ticket owner email field 
        self.open(base_url + '/logout')

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_submit_sell_ticket(self, *__):
        """
        Test Case: R3.6
        This test case tests the page contains selling form for tickets
        The selling form includes information: name, quantity, price, expiration date
        """
        #login by using the mock user
        self.login()
        self.open(base_url + '/')
        self.assert_text("Name")
        #test whether it include selling ticket name field 
        self.assert_element("#sell-name")
        self.assert_text("Quantity")
        #test whether it include selling ticket quantity field 
        self.assert_element("#sell-quantity")
        self.assert_text("Price")
        #test whether it include selling ticket price field 
        self.assert_element("#sell-price")
        self.assert_text("Expiration Date")
        #test whether it include selling ticket expiration date field 
        self.assert_element("#sell-date")
        #self.click('input[type="Submit Selling Ticket"]')
        self.open(base_url + '/logout')

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_submit_buy_ticket(self, *__):
        """
        Test Case: R3.7
        This test case tests the page contains buying form for tickets.
        The buying form includes information: name, quantity
        """
        #login by using the mock user
        self.login()
        self.open(base_url + '/')
        self.assert_text("Buying Ticket")
        #test whether it include buying ticket name field 
        self.assert_element("#buy-name")
        self.assert_text("Buying Quantity")
        #test whether it include buying ticket quantity field 
        self.assert_element("#buy-quantity")
        #self.click('input[type="Submit Buying Ticket"]')
        self.open(base_url + '/logout')


    def post_selling_form(self, *__):
        """
        !!! So far we can't test this specification, because we don't have data 
        Test Case: R3.8
        This test case tests whether the selling form can be posted on /sell
        """
        #self.login()
        #self.open(base_url + '/')
     
        
    def post_buying_form(self, *__):
        """
        Test Case: R3.9
        !!! So far we can't test this specification, because we don't have data 
        This test case tests whether the buying form can be posted on /buy
        """
        #self.login()
        #self.open(base_url + '/')
       

    def post_update_form(self, *__):
        """
        Test Case: R3.10
        !!! So far we can't test this specification, because we don't have data 
        This test case tests whether the update selling or buying form can be posted on /update
        """
        #self.login()
        #self.open(base_url + '/')
    



