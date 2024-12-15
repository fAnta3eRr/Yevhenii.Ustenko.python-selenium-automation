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


@when ('Click add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButtonOrTextIdFor']").click()
    sleep(5)


@when ('Confirm Add to Cart from side Navigation')
def confirm_add_to_cart_from_side(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AddToCart/FulfillmentSection'] [data-test='orderPickupButton']").click()


@when ('Open Cart Page')
def open_cart_page(context):
    context.driver.get('https://www.target.com/cart')


@then ('Verify cart has at list {amount} item(s)')
def verify_cart_has_item(context, amount):
    cart_page = context.driver.find_element(By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
    assert amount in cart_page, f"Expected {amount} items but got {cart_page}"
