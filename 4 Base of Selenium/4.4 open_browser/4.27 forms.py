import time

from selenium import webdriver
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
driver.get ('https://www.lambdatest.com/selenium-playground/simple-form-demo')
time.sleep (2)

# FORMS
# message = "Hello world!"
# input_field = driver.find_element(By.XPATH, "//input[@id='user-message']")
# input_field.send_keys(message)
# print("input field")
# time.sleep(2)
#
# button = driver.find_element(By.XPATH, "//button[@id='showInput']")
# button.click()
# print("button clicked")
# time.sleep(2)
#
# field_message = driver.find_element(By.XPATH, "(//p[@id='message'])")
# value_field_message = field_message.text
# print(value_field_message)
# assert value_field_message == message
# time.sleep(2)
# print("Success!")

# FORMS2
num_1 = 123
num_2 = 241

input_field_1 = driver.find_element (By.XPATH, "(//input[@id='sum1'])[1]")
input_field_1.send_keys (num_1)
print ("num_1")
time.sleep (2)

input_field_2 = driver.find_element (By.XPATH, "(//input[@id='sum2'])[1]")
input_field_2.send_keys (num_2)
print ("num_2")
time.sleep (2)

sum_button = driver.find_element (By.XPATH, "//button[contains(text(), 'Get Sum')]")
sum_button.click ()
print ("nums was summed")
time.sleep (2)

sum_field = driver.find_element (By.XPATH, "//p[@id='addmessage']")
value_field_message = sum_field.text
print (value_field_message)
sum = num_1 + num_2
assert value_field_message == str (sum)
time.sleep (2)
print ("Success!")

# QUIT
driver.quit ()
