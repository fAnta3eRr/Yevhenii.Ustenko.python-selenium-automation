from time import sleep

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from home_work2 import expected_result
from pages.base_page import BasePage


class CartPage(BasePage):


    CLICK_ON_CART = (By.XPATH, "//a[@data-test='@web/CartLink']")
    VERIFY_EMPTY_CART = (By.XPATH, "//h1[text()='Your cart is empty']")
    CLICK_TO_CART_BUTTON = (By.CSS_SELECTOR, "[id*='addToCartButtonOrTextIdFor']")
    CONFIRM_ADD_FROM_SIDE_NAVIGATION = (By.CSS_SELECTOR, "[data-test='@web/AddToCart/FulfillmentSection'] [data-test='orderPickupButton']")
    VERIFY_CART_HAS_ITEM = (By.XPATH, "//span[contains(text(), 'subtotal')]")
    PRODUCT_BY_NAME = (By.XPATH, "//div[@data-test='content-wrapper']//h4")
    PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


    def click_on_cart_icon(self):   #header
        self.wait_and_click(*self.CLICK_ON_CART)


    def verify_your_cart_is_empty(self):
       self.verify_text('Your cart is empty', *self.VERIFY_EMPTY_CART)


    def click_add_to_cart(self):
        self.wait_and_click(*self.CLICK_TO_CART_BUTTON)


    def add_product_name(self):
        #product_name = self.driver.wait.until(EC.visibility_of_element_located(self.PRODUCT_BY_NAME)).text
        #print(f'Product added: {product_name}')
        self.wait_for_element_visible(*self.PRODUCT_BY_NAME)


    def confirm_add_to_cart_from_side(self):
        self.wait_and_click(*self.CONFIRM_ADD_FROM_SIDE_NAVIGATION)


    def verify_cart_has_item(self, amount):
        #actual_result = self.find_element(*self.VERIFY_CART_HAS_ITEM).text
        #assert actual_result == amount, f'Expected {amount} not in actual {actual_result}'
        self.verify_text(amount, *self.VERIFY_CART_HAS_ITEM)


    def verify_cart_has_correct_product(self, product):
        self.verify_text(product, *self.PRODUCT_NAME_IN_CART)


