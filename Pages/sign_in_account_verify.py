from selenium.webdriver.common.by import By
from time import sleep
from Pages.base_page import Page

class Signin(Page):
    sign_in_account_message = (By.CSS_SELECTOR, "[class='sc-fe064f5c-0 sc-315b8ab9-2 WObnm gClYfs']")


    def verify_sign_account_message(self):
        self.verify_text('Sign into your Target account', *self.sign_in_account_message)
