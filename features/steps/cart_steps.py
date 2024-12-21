from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC



@when('Click on Cart icon')
def click_cart(context):
    context.app.cart_product_page.click_on_cart_icon()


@then('Verify "Your cart is empty" message is shown')
def verify_your_cart_is_empty(context):
    context.app.cart_product_page.verify_your_cart_is_empty()


@when ('Click add to cart button')
def click_add_to_cart(context):
    context.app.cart_product_page.click_add_to_cart()
    sleep(5)


@when ('Add product name')
def add_product_name(context):
    context.app.cart_product_page.add_product_name()


@when ('Confirm Add to Cart from side Navigation')
def confirm_add_to_cart_from_side(context):
    context.app.cart_product_page.confirm_add_to_cart_from_side()


@when ('Open Cart Page')
def open_cart_page(context):
    context.app.header_page.open_cart_page()


@then ('Verify cart has at list {amount} item(s)')
def verify_cart_has_item(context, amount):
    sleep(5)
    context.app.cart_product_page.verify_cart_has_item(amount)


@then ('Verify cart has correct {product}')
def verify_cart_has_correct_product(context, product):
    context.app.cart_product_page.verify_cart_has_correct_product(product)
