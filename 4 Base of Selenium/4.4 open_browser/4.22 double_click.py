import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
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
driver.get ('https://demoqa.com/buttons')
time.sleep (2)

# DOUBLE CLICK
action = ActionChains (driver)
double_click = driver.find_element (By.XPATH, "//button[@id='doubleClickBtn']")
action.double_click (double_click).perform ()
time.sleep (2)
print ("Double click")

# RIGHT CLICK
action = ActionChains (driver)
right_click = driver.find_element (By.XPATH, "//button[@id='rightClickBtn']")
action.context_click (right_click).perform ()
time.sleep (2)
print ("Right click")

# QUIT
driver.quit ()
