from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class SearchProduct(BasePage):


    SEARCH_FIELD = (By.ID, 'search')
    LISTINGS = (By.CSS_SELECTOR, "[data-test*='@web/site-top-of-funnel/ProductCardWrapper']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
    PRODUCT_IMG = (By.CSS_SELECTOR, 'img')
    PRODUCT_BY_NAME = (By.XPATH, "//div[@data-test='content-wrapper']//h4")
    FAVORITES_BTN = (By.CSS_SELECTOR, "[data-test='FavoritesButton']")
    FAVORITES_TOOLTIP_TXT = (By.XPATH, "//*[text()='Click to sign in and save']")
    SEARCH_RESULTS = (By.XPATH, "//div[@data-test='resultsHeading']")


    def open_main(self, url):
        self.driver.get(url)


    def verify_header_results(self, product):
        self.verify_text(product, self.SEARCH_RESULTS)


    def verify_product_name_img(self):
        # To see ALL listings (comment out if you only check top ones):
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        sleep(5)
        # Find all products:
        all_products = self.driver.find_elements(*self.LISTINGS)
        # print(all_products)
        assert len(all_products) > 0, 'No products found'

        for product in all_products:
            title = product.find_element(*self.PRODUCT_TITLE).text
            assert title != '', 'Product title not shown'
            # print(title)
            product.find_element(*self.PRODUCT_IMG)

    def verify_search_url(self, product):
        self.verify_partial_url(product)


    def get_product_name(self):
        return self.find_element(*self.PRODUCT_BY_NAME).text


    def hover_favorites_icon(self):
        #fav_icon = self.find_element(*self.FAVORITES_BTN)
        #actions = ActionChains(self.driver)
        #actions.move_to_element(fav_icon)
        #actions.perform()
        self.hover_element(*self.FAVORITES_BTN)


    def verify_search_results(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULTS)


    def verify_fav_tooltip(self):
        self.wait_for_element_visible(*self.FAVORITES_TOOLTIP_TXT)



