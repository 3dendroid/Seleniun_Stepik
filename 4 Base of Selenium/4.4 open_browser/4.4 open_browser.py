from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Service
s = Service()

# Driver
driver = webdriver.Chrome(options=options, service=s)
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

# Quit
driver.quit()
