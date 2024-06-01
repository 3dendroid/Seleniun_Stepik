import time
import datetime

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
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
driver.get('https://www.saucedemo.com/')

# ELEMENTS
login_standard_user = 'standard_user'
password_all = 'secret_sauce'

# USERNAME
username = driver.find_element(By.ID, 'user-name')  # by ID attribute
username.send_keys(login_standard_user)
time.sleep(3)
print("Input Login")

# PASSWORD
password = driver.find_element(By.XPATH, '//*[@id="password"]')  # by XPATH attribute
password.send_keys(password_all)
time.sleep(3)
print("Input Password")
password.send_keys(Keys.ENTER)
time.sleep(3)

# ACTION CHAINS
action = ActionChains(driver)
red_t_shirt = driver.find_element(By.XPATH, '//*[@id="item_3_title_link"]/div')
action.move_to_element(red_t_shirt).perform()
time.sleep(3)

# SCROLL
# driver.execute_script("window.scrollTo(0, 300)")
# print("Scroll to 300 down")
# time.sleep(3)

# SCREENSHOT
now_date = datetime.datetime.utcnow().strftime("%Y_%m_%d_%H_%M_%S")
name_screenshot = 'screenshot_' + now_date + '.png'
driver.save_screenshot('C:\\Users\\GIGACHAD\\PycharmProjects\\Seleniun_Stepik\\4 Base of Selenium\\4.4 open_browser\\screenshots\\' + name_screenshot)


# QUIT
driver.quit()
