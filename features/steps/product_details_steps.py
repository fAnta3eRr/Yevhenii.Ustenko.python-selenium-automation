from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep


@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.app.product_details_page.open_target(product_id)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    context.app.product_details_page.click_and_verify_colors()


@then('Verify user can choose shoe colors')
def click_and_verify_shoes_colors(context):
    context.app.product_details_page.click_and_verify_shoes_colors()


