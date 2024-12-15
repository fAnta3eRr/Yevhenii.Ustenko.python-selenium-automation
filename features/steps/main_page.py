from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(3)


@then('Verify search result shown for {product}')
def verify_header_results(context, product):
    element = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    print('\nFind element:')
    print(element)











