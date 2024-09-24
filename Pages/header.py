from selenium.webdriver.common.by import By
from time import sleep

from Pages.base_page import Page

class Header(Page):

    search_field=(By.ID, 'search')
    search_btn=(By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    click_cart_icon=(By.CSS_SELECTOR,"[href='/icons/Cart.svg#Cart']")
    sign_in= (By.CSS_SELECTOR, "[class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']")
    sign_in_sidebar=(By.CSS_SELECTOR,"[data-test='accountNav-signIn']")

    def search_product(self, product):
        self.input_text(product,*self.search_field)
        self.click(*self.search_btn)
        sleep(6)

    def click_cart(self):
        self.wait_to_be_clickable_click(*self.click_cart_icon)

    def click_sign_in(self):
        self.click(*self.sign_in)

    def click_side_menu_signin(self):
        self.click(*self.sign_in_sidebar)
        sleep(4)