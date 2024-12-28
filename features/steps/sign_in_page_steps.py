from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# Test navigate to Sign in form
@when ('Click Sign in')
def click_sign_in(context):
    context.app.sign_in_page.click_sign_in()


@then ('From right side navigation menu, click Sign in')
def navigation_click_sign_in(context):
     context.app.sign_in_page.navigation_click_sign_in()


@then ('Verify Sign in from opened')
def verify_sign_in_open(context):
    context.app.sign_in_page.verify_sign_in_open()


@then ('Input {email} and {password} on SignIn page')
def credentials(context, email, password):
    context.app.sign_in_page.credentials(email, password)


@then ('Click Sign in button')
def click_sign_in_button(context):
    context.app.sign_in_page.click_sign_in_button()


@then ('Verify user is logged in (sign in form should disappear)')
def verify_sign_in_form_disappear(context):
    context.app.sign_in_page.verify_sign_in_form_disappear()


@then ('Input incorrect credentials {email} and {password} combination')
def credentials(context, email, password):
    sleep(4)
    context.app.sign_in_page.credentials(email, password)

@then ('Verifies that {text} message is shown')
def incorrect_credentials_notification(context, text):
    context.app.sign_in_page.incorrect_credentials_notification(text)
