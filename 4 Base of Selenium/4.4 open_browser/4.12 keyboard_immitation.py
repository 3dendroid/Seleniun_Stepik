import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# OPTIONS
options = webdriver.ChromeOptions ()
options.add_experimental_option ('detach', True)
# options.add_argument('--headless')  # headless mode

# SERVICE
s = Service ()

# DRIVER
driver = webdriver.Chrome (options=options, service=s)
driver.maximize_window ()
driver.get ('https://www.saucedemo.com/')

# ELEMENTS
login_standard_user = 'standard_user'
password_all = 'secret_sauce'

# USERNAME
username = driver.find_element (By.ID, 'user-name')  # by ID attribute
username.send_keys (login_standard_user)
time.sleep (3)
print ("Input Login")

# PASSWORD
password = driver.find_element (By.XPATH, '//*[@id="password"]')  # by XPATH attribute
password.send_keys (password_all)
time.sleep (3)
print ("Input Password")
password.send_keys (Keys.ENTER)
time.sleep (3)

# FILTER
filter = driver.find_element (By.XPATH, '//select[@data-test=\"product-sort-container"]')  # by XPATH attribute
filter.click ()
print ("Click filter")
time.sleep (3)
filter.send_keys (Keys.DOWN)
time.sleep (3)
filter.send_keys (Keys.ENTER)
time.sleep (3)

# BUTTON
# button_login = driver.find_element(By.CSS_SELECTOR, '#login-button')  # by CSS attribute
# button_login.click()
# print("Click Login Button")


# QUIT
driver.quit ()
