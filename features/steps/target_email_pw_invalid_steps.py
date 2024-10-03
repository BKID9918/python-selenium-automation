from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on Sign In')
def click_sign_in(context):
    context.app.header.click_sign_in()
    sleep(3)

@when('Click Sign In on navigation menu')
def click_signin_from_navi_bar(context):
    context.app.header.click_side_menu_signin()
    sleep(3)

@when('Click on Email or mobile phone')
def click_on_email_field(context):
    context.app.email_pw_invalid.click_on_email_field()

@when('Enter email {text}')
def input_email(context,text):
    context.app.email_pw_invalid.input_email(text)

@when('Click on Password field')
def click_on_pw_field(context):
    context.app.email_pw_invalid.click_on_password_field()

@when('Enter password {text}')
def input_password(context, text):
    context.app.email_pw_invalid.input_pw(text)

@when('Click Sign in with password')
def click_signin_pw(context):
    context.app.email_pw_invalid.click_on_pw_signin_btn()
    sleep(3)

@then("Verify We can't find your account")
def verify_full_text(context):
    context.app.email_pw_invalid.verify_no_target_account()