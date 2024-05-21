from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Options
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument('--headless')  # headless mode

# Service
s = Service()

# Driver
driver = webdriver.Chrome(options=options, service=s)
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

# Elements
login_standard_user = 'standard_user'
password_all = 'secret_sauce'
# username
username = driver.find_element(By.ID, 'user-name')  # by ID attribute
username.send_keys(login_standard_user)
print("Input Login")
# password
password = driver.find_element(By.XPATH, '//*[@id="password"]')  # by XPATH attribute
password.send_keys(password_all)
print("Input Password")
# button
button_login = driver.find_element(By.CSS_SELECTOR, '#login-button')  # by CSS attribute
button_login.click()
print("Click Login Button")
# text
# text_products = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
# value_text_products = text_products.text
# print(value_text_products)
# assert value_text_products == "Products"
# print("GOOD!")
# url
url = 'https://www.saucedemo.com/inventory.html'
get_url = driver.current_url  # get current url
print(get_url)
assert url == get_url
print("SUCCESS!")

# Quit
driver.quit()
