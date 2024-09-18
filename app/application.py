from Pages.header import Header
from Pages.main_page import MainPage
from Pages.base_page import Page
from Pages.search_results_page import SearchResultsPage
from Pages.verify_cart_empty import VerifyEmptyCart


class Application:

    def __init__(self,driver):
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.header= Header(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.verify_cart_empty = VerifyEmptyCart(driver)