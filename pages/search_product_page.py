from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchProduct(BasePage):


    SEARCH_FIELD = (By.ID, 'search')
    VERIFY_SEARCH_RESULT = (By.XPATH, "//div[@data-test='resultsHeading']")
    LISTINGS = (By.CSS_SELECTOR, "[data-test*='@web/site-top-of-funnel/ProductCardWrapper']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
    PRODUCT_IMG = (By.CSS_SELECTOR, 'img')


    def open_main(self, url):
        self.driver.get(url)


    def verify_header_results(self, product):
        self.verify_text(product, self.VERIFY_SEARCH_RESULT)


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



