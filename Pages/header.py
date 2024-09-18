from selenium.webdriver.common.by import By
from time import sleep

from Pages.base_page import Page

class Header(Page):

    search_field=(By.ID, 'search')
    search_btn=(By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    click_cart_icon=(By.CSS_SELECTOR,"[href='/icons/Cart.svg#Cart']")

    def search_product(self, product):
        self.input_text(product,*self.search_field)
        self.click(*self.search_btn)
        sleep(6)

    def click_cart(self):
        self.click(*self.click_cart_icon)
        sleep(4)