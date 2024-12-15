from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click()


@then('Verify "Your cart is empty" message is shown')
def verify_your_cart_is_empty(context):
    print('n/Find element:')
    element = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    print(element)
    assert element == 'Your cart is empty'