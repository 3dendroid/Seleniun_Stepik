import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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
driver.get('https://demoqa.com/dynamic-properties')
time.sleep(2)

#  IMPLICIT EXPECTATION
# print("Start Test")
# driver.implicitly_wait(10)
# visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']")
# visible_button.click()
# print("Finish Test")

# EXPLICIT EXPECTATION
print("Start Test")
visible_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='visibleAfter']")))
visible_button.click()
print("Finish Test")

# QUIT
driver.quit()
