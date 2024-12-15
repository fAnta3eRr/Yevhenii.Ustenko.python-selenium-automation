from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


# Test navigate to Sign in form
@when ('Click Sign in')
def click_sign_in(context):
    context.driver.find_element(By.ID, "account-sign-in").click()


@then ('From right side navigation menu, click Sign in')
def click_sign_in(context):
     context.driver.find_element(By.CSS_SELECTOR, "button[data-test='accountNav-signIn']").click()


@then ('Verify Sign in from opened')
def verify_sign_in_open(context):
    expected_result = 'Sign into your Target account'
    actual_result = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'