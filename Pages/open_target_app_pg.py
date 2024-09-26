from selenium.webdriver.common.by import By
from time import sleep

from Pages.base_page import Page

class TargetAppPage(Page):
    pp_link=(By.CSS_SELECTOR, "[href='/c/target-privacy-policy/-/N-4sr7p']")


    def open_target_app_page(self):
        self.open_page('https://www.target.com/c/target-app/')

    def click_privacy_policy_link(self):
        self.wait_to_be_clickable_click(*self.pp_link)

    def verify_pp_partial_url(self):
        self.verify_partial_url('/c/target-privacy-policy/')