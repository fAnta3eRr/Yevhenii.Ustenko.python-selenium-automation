from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage


class HeaderPage(BasePage):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BUTTON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_PAGE_BUTTON = (By.CSS_SELECTOR, "[href='/cart']")


    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.wait_and_click(*self.SEARCH_BUTTON)
        sleep(10)

    def open_cart_page(self):
        self.wait_and_click(*self.CART_PAGE_BUTTON)
