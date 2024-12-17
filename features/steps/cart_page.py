from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

CLICK_ON_CART = (By.XPATH, "//a[@data-test='@web/CartLink']")
VERIFY_EMPTY_CART = (By.XPATH, "//h1[text()='Your cart is empty']")
CLICK_TO_CART_BUTTON = (By.CSS_SELECTOR, "[id*='addToCartButtonOrTextIdFor']")
CONFIRM_ADD_FROM_SIDE_NAVIGATION = (By.CSS_SELECTOR, "[data-test='@web/AddToCart/FulfillmentSection'] [data-test='orderPickupButton']")
VERIFY_CART_HAS_ITEM = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
PRODUCT_BY_NAME = (By.XPATH, "//div[@data-test='content-wrapper']//h4")
PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(*CLICK_ON_CART).click()


@then('Verify "Your cart is empty" message is shown')
def verify_your_cart_is_empty(context):
    print('n/Find element:')
    element = context.driver.find_element(*VERIFY_EMPTY_CART).text
    print(element)
    assert element == 'Your cart is empty'


@when ('Click add to cart button')
def click_add_to_cart(context):
    context.driver.wait.until(EC.visibility_of_element_located(CLICK_TO_CART_BUTTON)).click()


@when ('Add product name')
def add_product_name(context):
    context.product_name = context.driver.wait.until(EC.visibility_of_element_located(PRODUCT_BY_NAME)).text
    print(f'Product added: {context.product_name}')


@when ('Confirm Add to Cart from side Navigation')
def confirm_add_to_cart_from_side(context):
    context.driver.wait.until(EC.element_to_be_clickable(CONFIRM_ADD_FROM_SIDE_NAVIGATION)).click()


@when ('Open Cart Page')
def open_cart_page(context):
    context.driver.get('https://www.target.com/cart')


@then ('Verify cart has at list {amount} item(s)')
def verify_cart_has_item(context, amount):
    cart_page = context.driver.find_element(*VERIFY_CART_HAS_ITEM).text
    assert amount in cart_page, f"Expected {amount} items but got {cart_page}"


@then ('Verify cart has correct product')
def verify_cart_has_correct_product(context):
    actual_name = context.driver.find_element(*PRODUCT_NAME_IN_CART).text
    print(f'Actual product name: {actual_name}')
    print(f'Product stored earlier: {context.product_name}')
    assert context.product.name in actual_name, f"Actual product name {context.product_name} but got {actual_name}"
