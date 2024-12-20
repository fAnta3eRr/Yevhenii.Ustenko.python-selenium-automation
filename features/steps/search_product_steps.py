from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Open target main page')
def open_main(context):
    context.app.search_product_page.open_main('https://www.target.com/')


@when('Search for {product}')
def search_product(context, product):
    context.app.header_page.search_product('tide')
    sleep(5)


@then('Verify search result shown for {product}')
def verify_header_results(context, product):
    context.app.search_product_page.verify_header_results(product)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    context.app.search_product_page.verify_product_name_img()


@then('Verify search term {product} in URl')
def verify_search_url(context, product):
    context.app.search_product_page.verify_product(product)











