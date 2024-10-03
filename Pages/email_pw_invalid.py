from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Pages.base_page import Page

class EmailPwAccount(Page):
    EMAIL_INP = (By.CSS_SELECTOR, "[id='username']")
    PW_INP =(By.CSS_SELECTOR, "[id='password']")
    SIGNIN_W_PW = (By.CSS_SELECTOR, "[id='login']")
    CANT_FIND_ACCOUNT= (By.CSS_SELECTOR, "[role='alert']")



    def click_on_email_field (self):
         self.click(*self.EMAIL_INP)

    def click_on_password_field (self):
         self.click(*self.PW_INP)

    def input_email(self, text):
        self.input_text(text, *self.EMAIL_INP)

    def input_pw(self, text):
        self.input_text(text, *self.PW_INP)

    def click_on_pw_signin_btn(self):
        self.click(*self.SIGNIN_W_PW)

    def verify_no_target_account(self):
        self.verify_text("We can't find your account.",*self.CANT_FIND_ACCOUNT)




