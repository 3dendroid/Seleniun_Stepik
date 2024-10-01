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
driver.get ('https://demoqa.com/checkbox')

# CHECKBOX
checkbox = driver.find_element (By.XPATH, "//button[@aria-label='Toggle']")
checkbox.click ()
time.sleep (3)

# QUIT
driver.quit ()
