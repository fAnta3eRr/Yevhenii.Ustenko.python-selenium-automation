from pages.base_page import BasePage


class TermsAndConditions(BasePage):

    def verify_terms_and_conditions_opened(self):
        self.verify_partial_url('terms-conditions/')