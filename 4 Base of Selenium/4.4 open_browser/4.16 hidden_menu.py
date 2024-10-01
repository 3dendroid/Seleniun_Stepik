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
time.sleep (2)
print ("Input Login")

# PASSWORD
password = driver.find_element (By.XPATH, '//*[@id="password"]')  # by XPATH attribute
password.send_keys (password_all)
time.sleep (2)
print ("Input Password")
password.send_keys (Keys.ENTER)
time.sleep (2)

# MENU
menu = driver.find_element (By.XPATH, '//*[@id="react-burger-menu-btn"]')  # by XPATH attribute
menu.click ()
time.sleep (2)
print ("Click Menu button")

# ABOUT
about = driver.find_element (By.XPATH, '//*[@id="about_sidebar_link"]')  # by XPATH attribute
about.click ()
time.sleep (2)
print ("Click About link")

# QUIT
driver.quit ()
