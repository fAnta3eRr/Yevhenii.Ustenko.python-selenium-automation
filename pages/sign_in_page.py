from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pages.base_page import BasePage


class SignInPage(BasePage):


    VERIFY_SIGN_IN_Account = (By.CSS_SELECTOR, "button[id='createAccount']")
    CLICK_SIGN_IN = (By.CSS_SELECTOR, "button[data-test='accountNav-signIn']")
    SIDE_NAVIGATION_SIGN_IN = (By.ID, "account-sign-in")
    CLICK_SIGN_IN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    VERIFY_SIGN_IN_FORM_DISAPPEAR = (By.CSS_SELECTOR, "[for='keepMeSignedIn']")
    EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, "[id='username']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[data-test='login-password']")
    INCORRECT_NOTIFICATION = (By.XPATH, "//span[text()= 'Please enter a valid email or phone number']")


    def click_sign_in(self):
        self.wait_and_click(*self.SIDE_NAVIGATION_SIGN_IN)


    def navigation_click_sign_in(self):
        self.wait_and_click(*self.CLICK_SIGN_IN)


    def verify_sign_in_open(self):
        self.verify_text('Create your Target account', *self.VERIFY_SIGN_IN_Account)


    def click_sign_in_button(self):
        self.wait_and_click(*self.CLICK_SIGN_IN_BUTTON)


    def credentials(self, username, password):
        self.input_text(username, *self.EMAIL_INPUT_FIELD)
        self.input_text(password, *self.PASSWORD_FIELD)


    def verify_sign_in_form_disappear(self):
        self.wait_for_element_invisible(*self.VERIFY_SIGN_IN_FORM_DISAPPEAR)


    def incorrect_credentials_notification(self, text):
        self.verify_text(text, *self.INCORRECT_NOTIFICATION)



