from selenium.webdriver.common.by import By
from time import sleep
from Pages.base_page import Page

class ProductInCart(Page):

    cart_mean_item_in_cart=(By.CSS_SELECTOR, "[id='cart-summary-heading']")

    def verify_item_in_cart(self):
        self.verify_text('Cart', *self.cart_mean_item_in_cart)
