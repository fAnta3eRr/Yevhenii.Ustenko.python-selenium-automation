from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')

SEARCH_BUTTON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
VERIFY_SEARCH_RESULT = (By.XPATH, "//div[@data-test='resultsHeading']")


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(*SEARCH_BUTTON).click()
    sleep(5)


@then('Verify search result shown for {product}')
def verify_header_results(context, product):
    element = context.driver.find_element(*VERIFY_SEARCH_RESULT).text
    print('\nFind element:')
    print(element)











