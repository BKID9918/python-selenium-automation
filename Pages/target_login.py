from selenium.webdriver.common.by import By
from time import sleep

from Pages.base_page import Page

class TargetLogin(Page):
    t_and_c_link= (By.CSS_SELECTOR,"[href='/c/terms-conditions/-/N-4sr7l']")

    def open_target_login_url(self):
            self.open_page('https://www.target.com/login')

    def click_terms_and_conditions_link(self):
        self.click(*self.t_and_c_link)

    def verify_part_of_url(self):
        self.verify_partial_url('/c/terms-conditions/')


