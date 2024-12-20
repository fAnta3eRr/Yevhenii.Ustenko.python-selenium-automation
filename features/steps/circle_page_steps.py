from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open target circle page')
def open_circle_page(context):
    context.app.circle_page.open_circle_page('https://www.target.com/circle')


#@then('User sees at least 10 benefit cells')
#def verify_benefit_cells (context):
    #context.app.circle_page.verify_benefit_cells()


@then('User sees {expected_amount} benefit cells')
def verify_benefit_cells (context, expected_amount):
    context.app.circle_page.verify_benefit_cells(expected_amount)



