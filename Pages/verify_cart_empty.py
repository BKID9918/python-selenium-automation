from selenium.webdriver.common.by import By
from time import sleep

from Pages.base_page import Page


class VerifyEmptyCart(Page):
    actual_result=(By.CSS_SELECTOR,"[data-test='boxEmptyMsg']")

    def verify_cart_message(self):
        real_results = self.driver.find_element(*self.actual_result).text
        expected_result = 'Your cart is empty'
        assert expected_result in real_results, f'Expected {expected_result}, and got {real_results}'
        sleep(4)
