import time

from selenium import webdriver
from selenium.webdriver import ActionChains
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
driver.get('https://html5css.ru/howto/howto_js_rangeslider.php')
time.sleep(2)

# SLIDER
actions = ActionChains(driver)
slider_1 = driver.find_element(By.XPATH, '//input[@type="range"]')
actions.click_and_hold(slider_1).move_by_offset(50, 0).release().perform()
print("Slided")

time.sleep(2)
slider_2 = driver.find_element(By.XPATH, '//input[@id="id2"]')
actions.click_and_hold(slider_2).move_by_offset(40, 0).release().perform()
print("Slided")

time.sleep(2)
slider_3 = driver.find_element(By.XPATH, '//input[@id="id1"]')
actions.click_and_hold(slider_3).move_by_offset(-70, 0).release().perform()
print("Slided")

# QUIT
driver.quit()
