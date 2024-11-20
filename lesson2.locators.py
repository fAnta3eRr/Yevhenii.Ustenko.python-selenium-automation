from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.amazon.com/")

#Amazon logo
driver.find_element(By.XPATH, "//*[@aria-label='Amazon']" )

#Email field
driver.find_element(By.ID, 'ap_email')

#Continue button
driver.find_element(By.XPATH, "//input[@type='submit']")

#Conditions of use link
driver.find_element(By.XPATH, "//a[contains(text(), 'Conditions of Use') and @target='_blank' ]")

#Privacy Notice link
driver.find_element(By.XPATH, "//a[contains(text(), 'Privacy Notice') and @target='_blank' ]")

#Need help link
driver.find_element(By.XPATH, "//a[contains(text(), 'Help') and @target='_blank' ]")

#Forgot your password link
driver.find_element(By.XPATH, "//*[contains(text(), 'Forgot password?') and @class='a-link-normal']")

#Other issues with Sign-In link

#Create your Amazon account button
driver.find_element(By.ID,'createAccountSubmit' )
