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
driver.get ('https://the-internet.herokuapp.com/javascript_alerts')
time.sleep (2)

# ALERTS
# button_1 = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']")
# button_1.click()
# time.sleep(2)
# driver.switch_to.alert.accept()
# time.sleep(2)

button_2 = driver.find_element (By.XPATH, "//button[normalize-space()='Click for JS Confirm']")
button_2.click ()  # ok
time.sleep (2)

# driver.switch_to.alert.accept()  # ok
driver.switch_to.alert.dismiss ()  # cancel
time.sleep (2)

# QUIT
driver.quit ()
