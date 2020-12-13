import pytest
from seleniumbase import BaseCase
from selenium.webdriver.common.keys import Keys

from qa327_test.conftest import base_url

# integration testing: the test case interacts with the 
# browser, and test the whole system (frontend+backend).

@pytest.mark.usefixtures('server')

class TestIntegrationPosting(BaseCase):

    def register(self):
        """register new user"""
        self.open(base_url + '/register')
        self.type("#email", "test_post@test.com")
        self.type("#name", "testpost")
        self.type("#password", "TEST_post")
        self.type("#password2", "TEST_post")
        self.click('input[type="submit"]')

    def login(self):
        """login to profile"""
        self.open(base_url + '/login')
        self.type("#email", "test_post@test.com")
        self.type("#password", "TEST_post")
        self.click('input[type="submit"]')

    def post_ticket(self):
        """post ticket to sell"""
        self.type("#sell-name", "TESTposting")
        self.type("#sell-quantity", "50")
        self.type("#sell-price", "50")
        date = self.find_element("#sell-date")
        date.send_keys("2020", Keys.ARROW_RIGHT, "12", Keys.ARROW_RIGHT, "31")
        self.click('input[value="Submit Selling Ticket"]')

    def test_posting(self, *_):
        # Invalidate any existing sessions. 
        self.open(base_url + '/logout')

        self.register()
        # Assert registration successful. 
        self.assert_element("#message")
        self.assert_text("Please login", "#message")
        
        self.login()
        # Assert login successful. 
        self.assert_title("Profile")
        # Confirm welcome header present. 
        self.assert_element("#welcome-header")
        self.assert_text("Hi testpost !", "#welcome-header")
        # Confirm balance is 5000. 
        self.assert_element("#balance")
        self.assert_text("Your Balance: 5000", "#balance")


        self.post_ticket()
        # Assert ticket successfully posted to /sell. 
        self.assert_title("Submit Selling Ticket")

        # Return to profile. 
        self.open(base_url)
        # Assert new ticket information shown on the page. 
        self.assert_text("TESTposting")

        # Logout from current session. 
        self.open(base_url + '/logout')

        # Assert fail to access restricted pages.
        self.open(base_url)
        self.assert_title("Log In")


class TestIntegrationPurchasing(BaseCase):

    def register(self):
        """register new user"""
        self.open(base_url + '/register')
        self.type("#email", "test_purchase@test.com")
        self.type("#name", "testpurchase")
        self.type("#password", "TEST_purchase")
        self.type("#password2", "TEST_purchase")
        self.click('input[type="submit"]')

    def login(self):
        """login to profile"""
        self.open(base_url + '/login')
        self.type("#email", "test_purchase@test.com")
        self.type("#password", "TEST_purchase")
        self.click('input[type="submit"]')

    def purchase_ticket(self):
        self.type("#buy-name", "TESTposting")
        self.type("#buy-quantity", "10")
        self.click('input[value="Submit Buying Ticket"]')

    def test_purchasing(self, *_):
        # Invalidate any existing sessions. 
        self.open(base_url + '/logout')

        self.register()
        # Assert registration successful. 
        self.assert_element("#message")
        self.assert_text("Please login", "#message")
        
        self.login()
        # Assert login successful. 
        self.assert_title("Profile")
        # Confirm welcome header present. 
        self.assert_element("#welcome-header")
        self.assert_text("Hi testpurchase !", "#welcome-header")
        # Confirm balance is 5000. 
        self.assert_element("#balance")
        self.assert_text("Your Balance: 5000", "#balance")

        self.purchase_ticket()
        # Assert transaction information successfully posted to /buy. 
        self.assert_title("Submit Buying Ticket")

        # Logout from current session. 
        self.open(base_url + '/logout')

        # Assert fail to access restricted pages.
        self.open(base_url)
        self.assert_title("Log In")