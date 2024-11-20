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

sleep(2)

driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()

sleep(2)


#Verification
expected_result = 'Sign in with password'
actual_result = driver.find_element(By.ID, 'login').text
assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'
print('Test passed')

driver.quit()