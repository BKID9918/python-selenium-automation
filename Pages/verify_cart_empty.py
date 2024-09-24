from selenium.webdriver.common.by import By
from time import sleep
from Pages.base_page import Page


class VerifyEmptyCart(Page):
    actual_result=(By.CSS_SELECTOR,"[data-test='boxEmptyMsg']")

    def verify_cart_message(self):
        self.verify_text('Your cart is empty', *self.actual_result)
