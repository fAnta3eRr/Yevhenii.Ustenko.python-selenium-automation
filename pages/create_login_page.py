from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CreateLogin(BasePage):


    VALID_CREDENTIALS = (By.CSS_SELECTOR, "form[method='post'] div")
    VERIFY_SIGN_IN_FORM_DISAPPEAR = (By.CSS_SELECTOR, "[for='keepMeSignedIn']")
    EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, "[id='username']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[data-test='login-password']")


    def valid_credentials(self, username, password):
        self.input_text(username, *self.EMAIL_INPUT_FIELD)
        self.input_text(password, *self.PASSWORD_FIELD)


    def verify_sign_in_form_disappear(self):
        self.wait_for_element_invisible(*self.VERIFY_SIGN_IN_FORM_DISAPPEAR)


