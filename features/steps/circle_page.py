from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open target circle page')
def open_main(context):
    context.driver.get('https://www.target.com/circle')


#@then('User sees at least 10 benefit cells')
#def verify_benefit_cells (context):
#    benefit_cells = context.driver.find_elements(By.CSS_SELECTOR, "[class='cell-item-content']")
#    print('\nPrinting benefit cells:')
#    print(benefit_cells)
#    assert len(benefit_cells) >= 10, f'Expected at least 10 benefit cells, got {len(benefit_cells)}'


@then('User sees {expected_amount} benefit cells')
def verify_benefit_cells (context, expected_amount):
    benefit_cells = context.driver.find_elements(By.CSS_SELECTOR, "[class='cell-item-content']")
    print('\nPrinting benefit cells:')
    print(benefit_cells)
    assert len(benefit_cells) == int(expected_amount), f'Expected {expected_amount}, got {len(benefit_cells)}'



