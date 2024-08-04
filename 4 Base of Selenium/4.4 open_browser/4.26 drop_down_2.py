import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# OPTIONS
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
# options.add_argument('--headless')  # headless mode

# SERVICE
s = Service()

# DRIVER
driver = webdriver.Chrome(options=options, service=s)
driver.maximize_window()
driver.get('https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo')
time.sleep(2)

# CLICK DROP DOWN
click_drop = driver.find_element(By.XPATH, "//span[@aria-labelledby='select2-country-container']")
click_drop.click()
time.sleep(2)
print('Click drop down')

# CLICK COUNTRY
click_country = Select(driver.find_element(By.XPATH, "//select[@id='country']"))
click_country.select_by_visible_text('Japan')
time.sleep(2)
print('Japan selected')

# CLICK COUNTRY
input_country = driver.find_element(By.XPATH, "(//input[@class='select2-search__field'])[2]")
input_country.send_keys("Denmark")
time.sleep(2)
input_country.send_keys(Keys.RETURN)
print('Denmark inputted and selected')
time.sleep(2)

# QUIT
driver.quit()
