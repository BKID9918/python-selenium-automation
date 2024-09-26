from lib2to3.fixes.fix_input import context

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@given('Open Target App page')
def open_target_app_main_page(context):
    context.app.open_target_app_pg.open_target_app_page()

@given('Store original window')
def store_window(context):
    context.original_window = context.app.open_target_app_pg.get_current_window()
    print('Original window', context.original_window )

@when('Click Privacy Policy link')
def click_pp_link(context):
    context.app.open_target_app_pg.click_privacy_policy_link()

@when('Switch to new window')
def switch_to_window(context):
    sleep(4)
    context.app.open_target_app_pg.switch_to_new_window()
    print('current window', context.app.open_target_app_pg.get_current_window())

@then('Verify Privacy Policy page opened')
def verify_pp_page_opened(context):
    context.app.open_target_app_pg.verify_pp_partial_url()
    sleep(3)

@then('Close current page')
def close_page(context):
    context.app.open_target_app_pg.close()
    sleep(3)

@then('Return to original window')
def switch_back_to_original_window(context):
    context.app.open_target_app_pg.switch_to_window_by_id(context.original_window)
