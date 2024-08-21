import time

from faker import Faker
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
driver.get('https://www.saucedemo.com/')
time.sleep(2)

# Faker
faker = Faker("en_US")  # ru_RU if russian
name = faker.first_name() + str(faker.random_int())
print(name)

password = faker.password() + str(faker.random_int())
print(password)

# LOGIN, PASSWORD
input_username = driver.find_element(By.ID, 'user-name')  # by ID attribute
input_username.send_keys(name)
time.sleep(2)
print("Input Login")

input_password = driver.find_element(By.XPATH, '//*[@id="password"]')  # by XPATH attribute
input_password.send_keys(password)
input_password.send_keys(Keys.ENTER)
print("Input Password")
time.sleep(2)

# QUIT
driver.quit()
