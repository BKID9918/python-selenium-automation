from selenium.webdriver.common.by import By
from time import sleep

from Pages.base_page import Page

class Cart(Page):
    add_to_cart = (By.CSS_SELECTOR, 'div button[data-test="chooseOptionsButton"]')
    add_to_cart_side_menu = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
    prev_button = (By.CSS_SELECTOR, "[data-test='modal-drawer-previous-button']")
    click_x = (By.CSS_SELECTOR, "[aria-label='close']")
    click_cart_icon = (By.CSS_SELECTOR, "[href='/icons/Cart.svg#Cart']")

    def click_add_to_cart(self):
        self.click(*self.add_to_cart)

    def click_add_to_cart_side(self):
        self.click(*self.add_to_cart_side_menu)

    def previous_btn(self):
        self.click(*self.prev_button)

    def click_x_icon(self):
        self.click(*self.click_x)

    def click_cart_img(self):
        self.click(*self.click_cart_icon)