from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# SEARCH_INPUT = (By.NAME, 'q')
# SEARCH_SUBMIT = (By.NAME, 'btnK')
#
#
# @given('Open Google page')
# def open_google(context):
#     context.driver.get('https://www.google.com/')
#
#
# @when('Input {search_word} into search field')
# def input_search(context, search_word):
#     search = context.driver.find_element(*SEARCH_INPUT)
#     search.clear()
#     search.send_keys(search_word)
#
#Feature: Test Scenarios for Search functionality

#  Scenario: User can search for a product
#    Given Open Google page
#    When Input Car into search field
#    And Click on search icon
#    Then Product results for Car are shown

#  Scenario: open the Target Circle page
#    Given Open Target Circle page
#    Then Verify 10 benefit cells
# #
# Scenario Outline: User can add item to cart
#   Given Open target main page
#   When Search for <product>
#   When Add <product> to cart
#   Then Verify <product
# uzh-ykpw-ysn