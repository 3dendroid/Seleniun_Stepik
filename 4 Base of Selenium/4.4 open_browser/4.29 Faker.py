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
driver.get('https://www.lambdatest.com/selenium-playground/iframe-demo/')
time.sleep(2)

# Faker

# QUIT
driver.quit()
