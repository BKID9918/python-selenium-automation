from Pages.header import Header
from Pages.main_page import MainPage
from Pages.base_page import Page
from Pages.search_results_page import SearchResultsPage
from Pages.verify_cart_empty import VerifyEmptyCart
from Pages.sign_in_account_verify import Signin
from Pages.verify_product_in_cart import ProductInCart
from Pages.add_to_cart import Cart

class Application:

    def __init__(self,driver):
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.header= Header(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.verify_cart_empty = VerifyEmptyCart(driver)
        self.sign_in_account_verify = Signin(driver)
        self.verify_product_in_cart = ProductInCart(driver)
        self.add_to_cart = Cart(driver)

