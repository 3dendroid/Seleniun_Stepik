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
driver.get ('https://demoqa.com/radio-button')
time.sleep (3)

# RADIO BUTTON
radio_button = driver.find_element (By.XPATH, "//label[@for='yesRadio']")
radio_button.click ()
time.sleep (2)

# QUIT
driver.quit ()
