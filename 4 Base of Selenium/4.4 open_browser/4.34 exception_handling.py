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

# EXCEPTION 1
# try:
#     visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
#     visible_button.click()
# except NoSuchElementException as exception:
#     print("No such element found:", exception)
#     time.sleep(10)
#     driver.refresh()
#     visible_button.click()
#     print("Visible button clicked")

# EXCEPTION 2
try:
    yes_checkbox = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
    yes_checkbox.click()
    message = driver.find_element(By.XPATH, "//span[@class='text-success']")
    value_message = message.text
    assert value_message == "No"

except AssertionError as e:
    driver.refresh()
    yes_checkbox = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
    yes_checkbox.click()
    message = driver.find_element(By.XPATH, "//span[@class='text-success']")
    value_message = message.text
    print(value_message)
    assert value_message == "Yes"
    driver.close()
print("Test over")

# QUIT
driver.quit()
