import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# OPTIONS
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
# options.add_argument('--headless')  # headless mode

# SERVICE
s = Service()

# DRIVER
driver = webdriver.Chrome(options=options, service=s)
driver.maximize_window()
driver.get('https://www.saucelabs.com/')

# BACK
driver.back()
print("Go back")
time.sleep(3)

# FORWARD
driver.forward()
print("Go forward")
time.sleep(3)

# QUIT
driver.quit()
