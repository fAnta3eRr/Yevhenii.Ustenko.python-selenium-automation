from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('Search for tea')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)


@then('Verify search results shown')
def verify_search_results(context):
    expected_result = 'tea'
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'


#Homework #3  Test for clicks on the cart
@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click()


@then('Verify "Your cart is empty" message is shown')
def verify_your_cart_is_empty(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'


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