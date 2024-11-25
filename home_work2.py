from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from sample_script import search

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()



driver.get("https://www.target.com/")

#Signin button
driver.find_element(By.XPATH, "//a[@id='account-sign-in']").click()

sleep(3)

driver.find_element(By.XPATH, "//button[contains(text(), 'Sign in') and @type='button']").click()

sleep(3)

#Verification
expected_result = 'Sign into your Target account'
actual_result = driver.find_element(By.XPATH, "//h1/span[text()='Sign into your Target account']").text  # other locator: "//h1/span"
assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'
print('Test passed')

# "//h1/span"
# OR:
#driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")

# Make sure login button is shown
#driver.find_element(By.ID, 'login')

# Verify an element present:
#driver.find_element(By.XPATH, "//*[text()='Popular filters']")

driver.quit()