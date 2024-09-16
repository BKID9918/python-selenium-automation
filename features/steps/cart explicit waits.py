# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

#
# from time import sleep
#
# # get the path to the ChromeDriver executable
#
# #driver.implicitly_wait(4)
#
#
#
# add_to_cart=(By.CSS_SELECTOR, "[id*='addToCartButton']")
# add_to_cart_side_menu=(By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
# prev_button=(By.CSS_SELECTOR, "[data-test='modal-drawer-previous-button']")
# click_x=(By.CSS_SELECTOR,"[aria-label='close']")
# click_cart_icon=(By.CSS_SELECTOR,"[href='/icons/Cart.svg#Cart']")
#
# @given('Open target main page')
# def open_main(context):
#     context.driver.get('https://www.target.com/')
#
# @when('Search for {product}')
# def search_product(context, product):
#     # Search field => enter product
#     context.driver.find_element(By.ID, 'search').send_keys(product)
#     # Search button => click
#     context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
#      # wait for search results page to load
#
#
# @when('Add {product} to cart')
# def add_product(context, product):
#
#     # Find and click the "Add to Cart" button (update selector as per page structure)
#     context.driver.wait.until(EC.element_to_be_clickable(add_to_cart))
#     context.driver.find_element(*add_to_cart).click()
#
#     context.driver.wait.until(EC.visibility_of_element_located(add_to_cart_side_menu))
#     context.driver.find_element(*add_to_cart_side_menu).click()
#
#     # wait for the item to be added to the cart
#     context.driver.wait.until(EC.visibility_of_element_located(prev_button))
#     context.driver.find_element(*prev_button).click()
#
#     context.driver.wait.until(EC.element_to_be_clickable(click_x))
#     context.driver.find_element(*click_x).click()
#
#     context.driver.wait.until(EC.visibility_of_element_located(click_cart_icon))
#     context.driver.find_element(*click_cart_icon).click()
#
#
# @then('Verify {product} in cart')
# def verify_results(context, product):
#
#     actual_result = context.driver.find_element(By.CSS_SELECTOR, "[id='cart-summary-heading']").text
#     expected_result = 'Cart'
#     assert expected_result in actual_result, f"Expected '{expected_result}', but got '{actual_result}'"
