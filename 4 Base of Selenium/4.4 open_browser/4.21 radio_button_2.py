import time

from selenium import webdriver
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
driver.get ('https://testpages.herokuapp.com/styled/basic-html-form-test.html')
time.sleep (2)

# RADIO BUTTON
radio_button_1 = driver.find_element (By.XPATH, "//input[@value='rd1']")
radio_button_1.click ()
time.sleep (2)

radio_button_2 = driver.find_element (By.XPATH, "//input[@value='rd2']")
radio_button_2.click ()
time.sleep (2)

radio_button_3 = driver.find_element (By.XPATH, "//input[@value='rd3']")
radio_button_3.click ()
time.sleep (2)

# QUIT
driver.quit ()
