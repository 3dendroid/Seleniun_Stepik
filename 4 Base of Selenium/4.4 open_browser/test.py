import sys
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from items import *

# ITEMS IMPORTED FROM items.py

# ELEMENTS
login_standard_user = 'standard_user'
password_all = 'secret_sauce'

print("Приветствую тебя в нашем интернет магазине!")
print(
    "Выбери один из следующих товаров и укажи его номер: \n1 - Sauce Labs Backpack \n2 - Sauce Labs Bike Light \n3 - Sauce Labs Onesie \n4 - Test.allTheThings() T-Shirt \n5 - Fleece Jacket \n6 - Brown T-Shirt")
product = input()

# CHECK IF PRODUCT NUMBER IS DIGIT AND VALID
if product.isdigit() and int(product) >= 7:
    print("Такого товара нет. Проверьте корректность ввода.")
    sys.exit()

if product in items:
    print(f"Вы выбрали {items[product]}. Товар будет куплен.")
else:
    print("Такого товара нет. Проверьте корректность ввода.")
    sys.exit()


def main():
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

    # INPUT LOGIN AND PASSWORD
    username = driver.find_element(By.ID, 'user-name')  # by ID attribute
    username.send_keys(login_standard_user)
    print("INPUT LOGIN")
    time.sleep(2)

    password = driver.find_element(By.XPATH, '//*[@id="password"]')  # by XPATH attribute
    password.send_keys(password_all)
    password.send_keys(Keys.ENTER)
    print("INPUT PASSWORD")
    time.sleep(2)

    # FIND, SELECT, ADD TO CART
    if product in xpathes:
        xpath = xpathes[product]
        value_product = driver.find_element(By.XPATH, xpath)
        value_product = value_product.text
        print(value_product)
        time.sleep(2)

    if product in value_prices:
        value = value_prices[product]
        value_price_product = driver.find_element(By.XPATH, value)
        value_price_product = value_price_product.text
        print(value_price_product)
        time.sleep(2)

    if product in ids:
        id = ids[product]
        select_product = driver.find_element(By.XPATH, f"//button[@id='{id}']")
        select_product.click()
        print("Select product")
        time.sleep(2)

    # CART INFO, CHECK VALUE AND PRICE
    cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    cart.click()
    print("ENTER CART")
    time.sleep(2)

    if product in cart_xpathes:
        cart_id = cart_xpathes[product]
        cart_xpath = f"//*[@id='{cart_id}']/div"
        cart_value_product = driver.find_element(By.XPATH, cart_xpath)
        cart_value_product = cart_value_product.text
        print(cart_value_product)
        time.sleep(2)

    assert value_product == cart_value_product
    print("CART VALUE INFO IS GOOD")
    cart_price_product = driver.find_element(By.XPATH,
                                             "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
    cart_price_product = cart_price_product.text
    print(cart_price_product)

    assert value_price_product == cart_price_product
    print("CART PRICE INFO IS GOOD")
    time.sleep(2)

    # CHECKOUT, INPUT DATA
    checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
    checkout.click()
    print("CLICK CHECKOUT")
    time.sleep(2)

    first_name = driver.find_element(By.XPATH, "//*[@id='first-name']")
    first_name.send_keys('Denis')
    print("INPUT FIRST NAME")
    time.sleep(2)

    last_name = driver.find_element(By.XPATH, "//*[@id='last-name']")
    last_name.send_keys('Sazonov')
    print("INPUT LAST NAME")
    time.sleep(2)

    postal_code = driver.find_element(By.XPATH, "//*[@id='postal-code']")
    postal_code.send_keys('100500')
    print("INPUT ZIP")
    time.sleep(2)

    continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
    continue_button.click()

    # CART INFO, CHECK VALUE AND PRICE
    finish_value_product = driver.find_element(By.XPATH, xpath)
    finish_value_product = finish_value_product.text
    print(finish_value_product)
    assert value_product == finish_value_product
    print("FINAL VALUE INFO IS GOOD")
    time.sleep(2)

    # QUIT
    driver.quit()


if __name__ == "__main__":
    main()
