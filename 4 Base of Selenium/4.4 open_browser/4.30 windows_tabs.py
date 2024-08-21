import time

from selenium import webdriver
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
driver.get('https://demoqa.com/browser-windows')
time.sleep(2)

# SWITCHING TABS
# click_tab_button = driver.find_element(By.XPATH, "//button[@id='tabButton']")
# click_tab_button.click()
# print("Tab button clicked")
# print(driver.current_url)
#
# header_1 = driver.find_element(By.XPATH, "//h1[normalize-space()='Browser Windows']")
# print(header_1.text)
#
# # SWITCHING TO NEWLY OPENED TAB
# driver.switch_to.window(driver.window_handles[1])
# time.sleep(2)
#
# header_2 = driver.find_element(By.XPATH, "//h1[@id='sampleHeading']")
# print(header_2.text)
#
# driver.switch_to.window(driver.window_handles[1])
# print(driver.current_url)

# SWITCHING WINDOWS
click_windows_button = driver.find_element(By.XPATH, "//button[@id='windowButton']")
click_windows_button.click()
print("Window button clicked")
print(driver.current_url)
time.sleep(2)

header_1 = driver.find_element(By.XPATH, "//h1[normalize-space()='Browser Windows']")
print(header_1.text)

windows_1 = driver.window_handles[0]
windows_2 = driver.window_handles[1]

# SWITCHING TO NEWLY OPENED WINDOWS
driver.switch_to.window(windows_2)
print(driver.current_url)

header_2 = driver.find_element(By.XPATH, "//h1[@id='sampleHeading']")
print(header_2.text)
driver.switch_to.window(windows_1)
print(driver.current_url)

header_1 = driver.find_element(By.XPATH, "//h1[normalize-space()='Browser Windows']")
print(header_1.text)

# QUIT
driver.quit()
