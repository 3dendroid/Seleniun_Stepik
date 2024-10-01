import time

from selenium import webdriver
from selenium.webdriver import Keys
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
driver.get ('https://demoqa.com/date-picker')
time.sleep (2)

# CALENDAR
new_date = driver.find_element (By.XPATH, "//input[@id='datePickerMonthYearInput']")

for i in range (10):
    new_date.send_keys (Keys.BACKSPACE)
time.sleep (2)

new_date.send_keys ('07/07/2024')
time.sleep (2)

today = driver.find_element (By.XPATH, "//div[contains(@class,'react-datepicker__day--today')]")
today.click ()
time.sleep (2)

# QUIT
driver.quit ()
