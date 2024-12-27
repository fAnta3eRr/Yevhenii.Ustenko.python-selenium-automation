from behave import given, when, then


@given('Open sign in page')
def open_sign_in_page_url(context):
    context.app.terms_and_cond_from_sign_in_page.open_sign_in_page_url()


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.terms_and_cond_from_sign_in_page.get_current_window_handle()


@then('Click on Target terms and conditions link')
def verify_terms_and_conditions_opened(context):
    context.app.terms_and_cond_from_sign_in_page.click_terms_and_conditions()


@then ('Switch to the newly opened window')
def switch_newly_opened_window(context):
    context.app.terms_and_cond_from_sign_in_page.switch_to_new_window()


@then ('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_opened(context):
    context.app.terms_and_conditions.verify_terms_and_conditions_opened()


@then ('User can close new window and switch back to original')
def close_and_return_to_original_window(context):
    context.app.verify_terms_and_conditions_opened.switch_to_window_by_id(context.original_window)



