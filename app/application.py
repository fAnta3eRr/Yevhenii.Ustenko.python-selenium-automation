from pages.base_page import BasePage
from pages.cart_product_page import CartPage
from pages.header_page import HeaderPage
from pages.main_page import MainPage
from pages.search_product_page import SearchProduct
from pages.product_details_page import ProductDetails
from pages.sign_in_page import SignInPage
from pages.circle_page import CirclePage
from pages.create_login_page import CreateLogin


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.base_page = BasePage(driver)
        self.header_page = HeaderPage(driver)
        self.main_page = MainPage(driver)
        self.search_product_page = SearchProduct(driver)
        self.cart_product_page = CartPage(driver)
        self.product_details_page = ProductDetails(driver)
        self.sign_in_page = SignInPage(driver)
        self.circle_page = CirclePage(driver)
        self.create_login_page = CreateLogin(driver)