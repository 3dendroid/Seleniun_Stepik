import datetime
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# OPTIONS
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
# options.add_argument('--headless')  # headless mode

# SERVICE
s = Service()

# DRIVER
driver = webdriver.Chrome(options=options, service=s)
driver.maximize_window()
driver.get('https://demoqa.com/date-picker')
time.sleep(2)

# CALENDAR
new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
for i in range(10):
    new_date.send_keys(Keys.BACKSPACE)
time.sleep(2)

now_date = datetime.datetime.utcnow().strftime("%d")
now_month = datetime.datetime.utcnow().strftime("%m")
now_year = datetime.datetime.utcnow().strftime("%y")

print(now_date)
date = int(now_date) + 10

if date >= 31:
    date = 9

print(date)
time.sleep(2)

new_date.send_keys(f"{now_month}/{date}/{now_year}")
time.sleep(5)

# QUIT
driver.quit()
