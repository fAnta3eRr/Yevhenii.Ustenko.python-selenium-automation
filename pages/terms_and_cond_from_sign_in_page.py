from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from time import sleep


class TermsAndCondSignInPage(BasePage):

    TC_LINK = (By.CSS_SELECTOR, 'a[href*="/c/terms-conditions"][target="_blank"]')

    def open_sign_in_page_url(self):
        self.open_url('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin')

    def click_terms_and_conditions(self):
        sleep(5)
        self.wait_and_click(*self.TC_LINK)
