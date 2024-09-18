from selenium.webdriver.common.by import By

from Pages.base_page import Page


class SearchResultsPage(Page):

    search_results_header = (By.XPATH, "//div[@data-test='resultsHeading']")

    def verify_results(self, product):
        actual_result = self.driver.find_element(*self.search_results_header).text
        assert product in actual_result, f'Expected {product}, got actual {actual_result}'
