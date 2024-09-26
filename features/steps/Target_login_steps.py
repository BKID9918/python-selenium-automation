from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

# @given('Open sign in page')
# def open_target_login(context):
#     sleep(3)
#     context.app.target_login.open_target_login_url()

@when('Store original window')
def store_current_window(context):
    context.original_window = context.app.target_login.get_current_window()
    print('Original window', context.original_window)
    sleep(3)

@when('Click Sign In')
def click_sign_in(context):
    context.app.header.click_sign_in()
    sleep(3)


@when('Click Sign In form navigation menu')
def click_signin_from_navi_bar(context):
    context.app.header.click_side_menu_signin()
    sleep(3)

@when('Click on Target terms and conditions link')
def click_terms_and_cond_link(context):
    context.app.target_login.click_terms_and_conditions_link()
    sleep(3)

@when('Switch to the newly opened window')
def switch_to_new_open_window(context):
    context.app.target_login.switch_to_new_window()
    print('current window', context.app.open_target_app_pg.get_current_window())
    sleep(3)

@then('Verify Terms and Conditions page is opened')
def verify_t_and_c_page_opened(context):
    context.app.target_login.verify_part_of_url()

@then('User can close new window')
def close_new_window(context):
    context.app.target_login.close()

@then('Switch back to original window')
def switch_back_to_orig_window(context):
    context.app.target_login.switch_to_window_by_id(context.original_window)








