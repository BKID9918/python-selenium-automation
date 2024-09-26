from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


# add_to_cart=(By.ID, 'addToCartButton')
# add_to_cart = (By.CSS_SELECTOR, 'div button[data-test="chooseOptionsButton"]')
# add_to_cart_side_menu=(By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
# prev_button=(By.CSS_SELECTOR, "[data-test='modal-drawer-previous-button']")
# click_x=(By.CSS_SELECTOR,"[aria-label='close']")
# click_cart_icon=(By.CSS_SELECTOR,"[href='/icons/Cart.svg#Cart']")

@given('Open target main page')
def open_main(context):
    # context.driver.get('https://www.target.com/')
    context.app.main_page.open_main_page()


@when('Search for a {product}')
def search_product(context, product):
    # Search field => enter tea
    # context.driver.find_element(By.ID, 'search').send_keys('tea')
    # # Search button => click
    # context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    # sleep(5)  # wait for search results page to load
    context.app.header.search_product(product)


@then('Verify that correct {product} results shown')
def verify_results(context, product):
    # actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    # expected_result = 'tea'
    # assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'
    # sleep(4)
    context.app.search_results_page.verify_results(product)


@then('Verify product {product} in url')
def verify_results_url(context, product):
    # actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    # expected_result = 'tea'
    # assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'
    # sleep(4)
    context.app.search_results_page.verify_results_of_url(product)


@when('Click on Cart icon')
def click_cart(context):
    # context.driver.find_element(By.CSS_SELECTOR, "[href='/icons/Cart.svg#Cart']").click()
    # sleep(4)
    context.app.header.click_cart()

@then('Verify “Your cart is empty” message')
def verify_cart_message(context):
    # real_results= context.driver.find_element(By.CSS_SELECTOR,"[class='sc-fe064f5c-0 dtCtuk']").text
    # expected_result= 'Cart'
    # assert expected_result in real_results, f'Expected {expected_result}, and got {real_results}'
    # sleep(4)
    context.app.verify_cart_empty.verify_cart_message()

# @when('Click Sign In')
# def click_sign_in(context):
#     context.app.header.click_sign_in()
#
#
# @when('Click Sign In form navigation menu')
# def click_signin_from_navi_bar(context):
#     context.app.header.click_side_menu_signin()


@then('Verify Sign In form opened')
def verify_login_page_message(context):
    context.app.sign_in_account_verify.verify_sign_account_message()


@given('Open Target Circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify {expected_amount} benefit cells')
def verify_found_results_text(context, expected_amount):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[class*='fBbzFg']")
    expected_amount = int(expected_amount)
    assert len(links) == int(expected_amount), f'Expected {expected_amount} links but got {len(links)}'



@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product(product)


@when('Add {product} to cart')
def add_product(context, product):
    sleep(7)
    # Find and click the "Add to Cart" button (update selector as per page structure)
    context.app.add_to_cart.click_add_to_cart()

    # context.driver.find_element(*add_to_cart).click()
    # sleep(7)
    context.app.add_to_cart.click_add_to_cart_side()    # # context.driver.find_element(*add_to_cart_side_menu).click()
    # sleep(7)

    # wait for the item to be added to the cart
    context.app.add_to_cart.previous_btn()    # context.driver.find_element(*prev_button).click()
    # sleep(7)
    context.app.add_to_cart.click_x_icon()
    # context.driver.wait.until(EC.element_to_be_clickable(click_x)).click()
    # context.driver.find_element(*click_x).click()
    # sleep(7)
    context.app.add_to_cart.click_cart_img()
    # context.driver.wait.until(EC.visibility_of_element_located(click_cart_icon)).click()
    # context.driver.find_element(*click_cart_icon).click()
    #
    # sleep(7)

@then('Verify {product} in cart')
def verify_results(context, product):

    context.app.verify_product_in_cart.verify_item_in_cart()
    # actual_result = context.driver.find_element(By.CSS_SELECTOR, "[id='cart-summary-heading']").text
    # expected_result = 'Cart'
    # assert expected_result in actual_result, f"Expected '{expected_result}', but got '{actual_result}'"
