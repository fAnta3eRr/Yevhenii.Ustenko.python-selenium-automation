from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from time import sleep


class TermsAndCondSignInPage(BasePage):

    TC_LINK = (By.CSS_SELECTOR, 'a[href*="/c/terms-conditions"][target="_blank"]')
    SIGNIN_BTN = (By.ID, 'account-sign-in')
    SIDENAV_SIGNIN_BTN = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')

    def open_sign_in_page_url(self):
        self.open_url('https://www.target.com')
        self.wait_and_click(*self.SIGNIN_BTN)
        self.wait_and_click(*self.SIDENAV_SIGNIN_BTN)


    def click_terms_and_conditions(self):
        self.wait_and_click(*self.TC_LINK)
