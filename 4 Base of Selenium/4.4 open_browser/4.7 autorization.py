import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Options
options = webdriver.ChromeOptions ()
options.add_experimental_option ("detach", True)

# Service
s = Service ()

# Driver
driver = webdriver.Chrome (options=options, service=s)
driver.maximize_window ()
driver.get ('https://www.saucedemo.com/')

# Elements
username = driver.find_element (By.ID, 'user-name')  # by ID attribute
username.send_keys ('standard_user')
time.sleep (3)

password = driver.find_element (By.ID, 'password')  # by ID attribute
password.send_keys ('secret_sauce')
time.sleep (3)

# button_login = driver.find_element(By.ID, 'login-button') # by ID attribute
# button_login.click()
# time.sleep(3)
button_login = driver.find_element (By.CSS_SELECTOR, '#login-button')  # by CSS attribute
button_login.click ()
time.sleep (3)

# Quit
driver.quit ()
