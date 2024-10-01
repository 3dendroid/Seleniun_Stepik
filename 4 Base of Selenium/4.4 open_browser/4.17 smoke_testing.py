import time

from selenium import webdriver
from selenium.webdriver import Keys
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
driver.get ('https://www.saucedemo.com/')

# ELEMENTS
login_standard_user = 'standard_user'
password_all = 'secret_sauce'

# USERNAME
username = driver.find_element (By.ID, 'user-name')  # by ID attribute
username.send_keys (login_standard_user)
time.sleep (2)
print ("Input Login")

# PASSWORD
password = driver.find_element (By.XPATH, '//*[@id="password"]')  # by XPATH attribute
password.send_keys (password_all)
time.sleep (2)
print ("Input Password")
password.send_keys (Keys.ENTER)
time.sleep (2)

# FIND, SELECT, ADD TO CART
value_product_1 = driver.find_element (By.XPATH, "//*[@id='item_4_title_link']/div")
value_product_1 = value_product_1.text
print (value_product_1)

value_price_product_1 = driver.find_element (By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = value_price_product_1.text
print (value_price_product_1)

select_product_1 = driver.find_element (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
select_product_1.click ()
time.sleep (2)

cart = driver.find_element (By.XPATH, "//a[@class='shopping_cart_link']")
cart.click ()
print ("Enter cart")
time.sleep (2)

# CART INFO, CHECK VALUE AND PRICE
cart_value_product_1 = driver.find_element (By.XPATH, "//*[@id='item_4_title_link']/div")
cart_value_product_1 = cart_value_product_1.text
print (cart_value_product_1)
assert value_product_1 == cart_value_product_1
print ("CART VALUE INFO IS GOOD")

cart_price_product_1 = driver.find_element (By.XPATH,
                                            "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
cart_price_product_1 = cart_price_product_1.text
print (cart_price_product_1)
assert value_price_product_1 == cart_price_product_1
print ("CART PRICE INFO IS GOOD")

# CHECKOUT
checkout = driver.find_element (By.XPATH, "//button[@id='checkout']")
checkout.click ()
print ("Click checkout")
time.sleep (2)

# INPUT DATA
first_name = driver.find_element (By.XPATH, "//*[@id='first-name']")
first_name.send_keys ('Denis')
print ("Input first name")

last_name = driver.find_element (By.XPATH, "//*[@id='last-name']")
last_name.send_keys ('Sazonov')
print ("Input last name")

postal_code = driver.find_element (By.XPATH, "//*[@id='postal-code']")
postal_code.send_keys ('100500')
print ("Input ZIP")
time.sleep (2)

continue_button = driver.find_element (By.XPATH, "//input[@id='continue']")
continue_button.click ()
time.sleep (2)

# CART INFO, CHECK VALUE AND PRICE
finish_value_product_1 = driver.find_element (By.XPATH, "//*[@id='item_4_title_link']/div")
finish_value_product_1 = finish_value_product_1.text
print (finish_value_product_1)
assert value_product_1 == finish_value_product_1
print ("FINAL VALUE INFO IS GOOD")

finish_price_product_1 = driver.find_element (By.XPATH,
                                              "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div")
finish_price_product_1 = finish_price_product_1.text
print (finish_price_product_1)
assert value_price_product_1 == finish_price_product_1
print ("FINAL PRICE INFO IS GOOD")

summary_price = driver.find_element (By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]")
value_summary_price = summary_price.text
print (value_summary_price)
item_total = "Item total: " + value_price_product_1
print (item_total)
assert value_summary_price == item_total
print ("SUCCESS!")

# QUIT
driver.quit ()
