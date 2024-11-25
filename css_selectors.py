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

# CSS
driver.find_element(By.ID, "twotabsearchtextbox")
# CSS, by id:
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
# CSS, by id & tag
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox")
# CSS, by class
driver.find_element(By.CSS_SELECTOR, '.nav-progressive-attribute')
driver.find_element(By.CSS_SELECTOR, '.nav-progressive-attribute.nav-input')
# CSS, by tag and class
driver.find_element(By.CSS_SELECTOR, 'input.nav-progressive-attribute.nav-input')
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox.nav-progressive-attribute.nav-input')

# CSS, by attributes
driver.find_element(By.CSS_SELECTOR, "[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
driver.find_element(By.CSS_SELECTOR, "a[data-csa-c-content-id='nav_cs_bestsellers']")
driver.find_element(By.CSS_SELECTOR, "a.nav-a[data-csa-c-content-id='nav_cs_bestsellers']")

# by CSS, attr partial match => *=
driver.find_element(By.CSS_SELECTOR, "a[href*='nav_cs_bestsellers']")
# keep in mind, you can access class as attributes:
driver.find_element(By.CSS_SELECTOR, "[class*='styles_baseCell'][class*='styles_cellSkinny']")

# By CSS selector, from parent node => to child
driver.find_element(By.CSS_SELECTOR, "[data-module-type='ProductListGrid'] h2")


# Homework #3 CSS Locators/ Create Account on Amazon.com (Registration)

# Amazon logo
driver.find_element(By.CSS_SELECTOR, ".a-section.a-padding-medium")

# Create account logo
driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']" )

# name field
driver.find_element(By.CSS_SELECTOR, "input[type=text]")

# email field
driver.find_element(By.CSS_SELECTOR, "input[type=email]")

# password field
driver.find_element(By.CSS_SELECTOR, "input[name=password]")

# Enter a password name
driver.find_element(By.XPATH, "//div[contains(text(), 'Enter a password') and @class='a-alert-content']")

# re-enter password
driver.find_element(By.CSS_SELECTOR, "input[type*='password'][id*='ap_password_check']")

# Continue button
driver.find_element(By.ID, "#continue")

# Conditions of Use button
driver.find_element(By.XPATH, "//a[text()= 'Conditions of Use']")

# Privacy Notice button
driver.find_element(By.XPATH, "//a[text()= 'Privacy Notice']")

# Sign in button
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")