from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CreateLogin(BasePage):


    VALID_CREDENTIALS = (By.CSS_SELECTOR, "form[method='post'] div")
    VERIFY_SIGN_IN_FORM_DISAPPEAR = (By.CSS_SELECTOR, "button[id='createAccount']")


    def valid_credentials(self, username, password, *locator):
        self.valid_credentials('olgatimanovska13@gmail.com', 'Timanovska1308', *self.VALID_CREDENTIALS)


    def verify_sign_in_form_disappear(self):
        self.wait.until(EC.invisibility_of_element_located(*self.VERIFY_SIGN_IN_FORM_DISAPPEAR))


