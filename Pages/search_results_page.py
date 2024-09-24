from selenium.webdriver.common.by import By
from Pages.base_page import Page


class SearchResultsPage(Page):

    search_results_header = (By.XPATH, "//div[@data-test='resultsHeading']")

    def verify_results(self, product):
        self.verify_partial_text(product ,*self.search_results_header)

    def verify_results_of_url(self, product):
        self.verify_partial_url(product)