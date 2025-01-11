from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from app.application import Application
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from support.logger import logger

# Command to run tests with Allure & Behave:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/target_search.feature

def browser_init(context):       # BROWSERSTACK  add(scenario_name)
    """
    :param context: Behave context
    """
    #Chrome
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    #Firefox
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    #logger
    # Enable capturing of the browser logs:
    # chrome_options = Options()
    # chrome_options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
    #
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service, options=chrome_options)

    ### HEADLESS MODE ####

    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #    options=options,
    #    service=service
    # )

    ### BROWSERSTACK ###

    #Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings

    #bs_user = 'yevheniiustenko_S2NqLi'
    #bs_key = 'BkgrTJpGVAJ9qxorVxKX'
    #url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    #options = Options()
    #bstack_options = {
    #    "os" : "OS X",
    #    "osVersion" : "Sequoia",
    #    'browserName': 'Chrome',
    #    'browserVersion' : 'latest',
    #    'sessionName': scenario_name,
    #}
    #options.set_capability('bstack:options', bstack_options)
    #context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver,  15)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    #logger.info(f'Started scenario: {scenario.name}')
    browser_init(context)    #BROWSERSTACK or logger  add(scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    #logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        #logger.error(f'Step failed: {step}')


def after_scenario(context, feature):
    # Add browser logs:          # logger
    # browser_logs = context.driver.get_log('browser')
    # with open("browser_logs.txt", "w") as log_file:
    #     for log_entry in browser_logs:
    #         log_file.write(f"{log_entry['level']} - {log_entry['timestamp']} - {log_entry['message']}\n")
    # print("Browser logs have been saved to browser_logs.txt")

    context.driver.quit()


    #(run the tests in terminal)

    #behave
    #behave features/tests/cart_tests.feature
    #behave -t smoke

    # Allure quick start (command in terminal)

    #behave -f allure_behave.formatter:AllureFormatter -o test_results
    #allure serve test_results/
    
    #behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features
    # allure serve %allure_result_folder%