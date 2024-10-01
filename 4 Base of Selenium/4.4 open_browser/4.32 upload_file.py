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
driver.get ('https://www.lambdatest.com/selenium-playground/upload-file-demo')
time.sleep (2)

# UPLOAD
button = driver.find_element (By.XPATH, "//input[@id='file']")
path = r'C:\Users\GIGACHAD\PycharmProjects\Seleniun_Stepik\4 Base of Selenium\4.4 open_browser\cat.jpg'  # path to upload file
button.send_keys (path)
time.sleep (2)

# QUIT
driver.quit ()
