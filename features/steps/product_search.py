from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


# add_to_cart=(By.ID, 'addToCartButton')
add_to_cart = (By.CSS_SELECTOR, 'div button[data-test="chooseOptionsButton"]')
add_to_cart_side_menu=(By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
prev_button=(By.CSS_SELECTOR, "[data-test='modal-drawer-previous-button']")
click_x=(By.CSS_SELECTOR,"[aria-label='close']")
click_cart_icon=(By.CSS_SELECTOR,"[href='/icons/Cart.svg#Cart']")

@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')




@when('Search for a product')
def search_product(context):
    # Search field => enter tea
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    # Search button => click
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)  # wait for search results page to load


@then('Verify that correct search results shown')
def verify_results(context):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    expected_result = 'tea'
    assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'
    sleep(4)


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href='/icons/Cart.svg#Cart']").click()
    sleep(4)


@then('Verify “Your cart is empty” message')
def verify_cart_message(context):
    real_results= context.driver.find_element(By.CSS_SELECTOR,"[class='sc-fe064f5c-0 dtCtuk']").text
    expected_result= 'Cart'
    assert expected_result in real_results, f'Expected {expected_result}, and got {real_results}'
    sleep(4)


@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']").click()


@when('Click Sign In form navigation menu')
def click_signin_from_navi_bar(context):
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='accountNav-signIn']").click()


@then('Verify Sign In form opened')
def verify_login_page_message(context):
    factual_results= context.driver.find_element(By.CSS_SELECTOR,"[class='sc-fe064f5c-0 sc-315b8ab9-2 WObnm gClYfs']").text
    expected_answer='Sign into your Target account'
    assert expected_answer in factual_results, f'Expected {expected_answer} but got {factual_results}'


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
    # Search field => enter product
    context.driver.find_element(By.ID, 'search').send_keys(product)
    # Search button => click
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
     # wait for search results page to load


@when('Add {product} to cart')
def add_product(context, product):
    sleep(7)
    # Find and click the "Add to Cart" button (update selector as per page structure)
    context.driver.wait.until(EC.element_to_be_clickable(add_to_cart)).click()

    # context.driver.find_element(*add_to_cart).click()
    # sleep(7)
    context.driver.wait.until(EC.visibility_of_element_located(add_to_cart_side_menu)).click()
    # # context.driver.find_element(*add_to_cart_side_menu).click()
    # sleep(7)

    # wait for the item to be added to the cart
    context.driver.wait.until(EC.visibility_of_element_located(prev_button)).click()
    # context.driver.find_element(*prev_button).click()
    # sleep(7)
    #
    context.driver.wait.until(EC.element_to_be_clickable(click_x)).click()
    # context.driver.find_element(*click_x).click()
    # sleep(7)

    context.driver.wait.until(EC.visibility_of_element_located(click_cart_icon)).click()
    # context.driver.find_element(*click_cart_icon).click()
    #
    # sleep(7)

@then('Verify {product} in cart')
def verify_results(context, product):

    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[id='cart-summary-heading']").text
    expected_result = 'Cart'
    assert expected_result in actual_result, f"Expected '{expected_result}', but got '{actual_result}'"
