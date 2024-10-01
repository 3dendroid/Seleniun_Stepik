import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# OPTIONS
path = r'C:\Users\GIGACHAD\PycharmProjects\Seleniun_Stepik\4 Base of Selenium\4.4 open_browser\files_download'
prefs = {'download.default_directory': path}
options = webdriver.ChromeOptions ()
options.add_experimental_option ('detach', True)
options.add_experimental_option ('prefs', prefs)
# options.add_argument('--headless')  # headless mode

# SERVICE
s = Service ()

# DRIVER
driver = webdriver.Chrome (options=options, service=s)
driver.maximize_window ()
driver.get ('https://www.lambdatest.com/selenium-playground/download-file-demo')
time.sleep (2)

# DOWNLOAD
button = driver.find_element (By.XPATH, "//button[contains(text(), 'Download File')]")
button.click ()
time.sleep (2)

# if os.listdir(path):
#     print("File exist")
# else:
#     print("File not exist")

file_name = 'Lambdatest.pdf'
assert os.access (path, os.F_OK) == True
print (f"File '{file_name}' downloaded successfully")

# QUIT
driver.quit ()
