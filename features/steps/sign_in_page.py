from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

VERIFY_SIGN_IN_Account = (By.XPATH, "//*[@data-test='accountNav-createAccount']")
CLICK_SIGN_IN = (By.CSS_SELECTOR, "button[data-test='accountNav-signIn']")
SIDE_NAVIGATION_SIGN_IN = (By.ID, "account-sign-in")

# Test navigate to Sign in form
@when ('Click Sign in')
def click_sign_in(context):
    context.driver.find_element(*SIDE_NAVIGATION_SIGN_IN).click()


@then ('From right side navigation menu, click Sign in')
def click_sign_in(context):
     context.driver.wait.until(EC.element_to_be_clickable(CLICK_SIGN_IN)).click()


@then ('Verify Sign in from opened')
def verify_sign_in_open(context):
    expected_result = 'Create account'
    actual_result = context.driver.wait.until(EC.visibility_of_any_elements_located(VERIFY_SIGN_IN_Account))
    assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'

