from Pages.email_pw_invalid import EmailPwAccount
from Pages.header import Header
from Pages.main_page import MainPage
from Pages.base_page import Page
from Pages.search_results_page import SearchResultsPage
from Pages.verify_cart_empty import VerifyEmptyCart
from Pages.sign_in_account_verify import Signin
from Pages.verify_product_in_cart import ProductInCart
from Pages.add_to_cart import Cart
from Pages.open_target_app_pg import TargetAppPage
from Pages.target_login import TargetLogin
from Pages.help_page import HelpPage
from Pages.email_pw_invalid import EmailPwAccount
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
        self.open_target_app_pg = TargetAppPage(driver)
        self.target_login = TargetLogin(driver)
        self.help_page = HelpPage(driver)
        self.email_pw_invalid = EmailPwAccount(driver)


