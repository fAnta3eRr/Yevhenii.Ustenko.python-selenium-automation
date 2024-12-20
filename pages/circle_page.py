from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage


class CirclePage(BasePage):


    BENEFIT_CELLS = (By.CSS_SELECTOR, "[class='cell-item-content']")


    def open_circle_page(self, url):
            self.driver.get(url)


    # def verify_benefit_cells (self):
    #    benefit_cells = self.driver.find_elements(*self.BENEFIT_CELLS)
    #    print('\nPrinting benefit cells:')
    #    print(benefit_cells)
    #    assert len(benefit_cells) >= 10, f'Expected at least 10 benefit cells, got {len(benefit_cells)}'


    def verify_benefit_cells(self, expected_amount):
        benefit_cells = self.driver.find_elements(*self.BENEFIT_CELLS)
        print('\nPrinting benefit cells:')
        print(benefit_cells)
        assert len(benefit_cells) == int(expected_amount), f'Expected {expected_amount}, got {len(benefit_cells)}'

