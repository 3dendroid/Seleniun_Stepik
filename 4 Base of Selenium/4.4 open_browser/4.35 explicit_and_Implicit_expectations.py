import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# OPTIONS
path = r'C:\Users\GIGACHAD\PycharmProjects\Seleniun_Stepik\4 Base of Selenium\4.4 open_browser\files_download'
prefs = {'download.default_directory': path}
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_experimental_option('prefs', prefs)
options.page_load_strategy = 'eager'
# options.add_argument('--headless')

# SERVICE
s = Service()

# DRIVER
driver = webdriver.Chrome(options=options, service=s)
driver.maximize_window()
# driver.get('https://demoqa.com/dynamic-properties')
driver.get('https://demoqa.com/radio-button')
time.sleep(2)

# EXPLICIT EXPECTATION

# IMPLICIT EXPECTATION


# QUIT
driver.quit()
