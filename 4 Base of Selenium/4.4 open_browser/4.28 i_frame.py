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
driver.get('https://www.lambdatest.com/selenium-playground/iframe-demo/')
time.sleep(2)

# iFRAMES
imframe = driver.find_element(By.XPATH, "//iframe[@id='iFrame1']")
driver.switch_to.frame(imframe)
time.sleep(2)

field = driver.find_element(By.XPATH, "//div[@id='__next']/div/div[2]")
field_value = field.text
print(field_value)

field.send_keys(Keys.CONTROL + 'a')

edition_panel_bold = driver.find_element(By.XPATH, "//button[@title='Bold']")
edition_panel_bold.click()
print('Bold button clicked')
time.sleep(2)

edition_panel_bold = driver.find_element(By.XPATH, "//button[@title='Italic']")
edition_panel_bold.click()
print('Italic button clicked')
time.sleep(2)

new_field = driver.find_element(By.XPATH, "//div[@id='__next']/div/div[2]/b")
new_field_value = new_field.text
print(new_field_value)
assert field_value == new_field_value
print("SUCCESS!")

# QUIT
driver.quit()
