import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = 'https://www.saucedemo.com/'


class Test_1:
    def test_successful_authorization(self):
        # OPTIONS
        options = webdriver.ChromeOptions ()
        options.add_experimental_option ('detach', True)

        # SERVICE
        s = Service ()

        # DRIVER
        driver = webdriver.Chrome (options=options, service=s)
        driver.maximize_window ()
        driver.get (url)
        time.sleep (2)

        # LOGIN, PASSWORD AND CLICK LOGIN BUTTON
        username = driver.find_element (By.ID, 'user-name')
        username.send_keys ('standard_user')

        password = driver.find_element (By.ID, 'password')
        password.send_keys ('secret_sauce')

        driver.find_element (By.ID, 'login-button').click ()
        time.sleep (2)

        print ('TEST IS OVER')
        driver.quit ()

    def test_fail_authorization(self):
        # OPTIONS
        options = webdriver.ChromeOptions ()
        options.add_experimental_option ('detach', True)

        # SERVICE
        s = Service ()

        # DRIVER
        driver = webdriver.Chrome (options=options, service=s)
        driver.maximize_window ()
        driver.get (url)
        time.sleep (2)

        # LOGIN, PASSWORD AND CLICK LOGIN BUTTON
        username = driver.find_element (By.ID, 'user-name')
        username.send_keys ('standard_use')

        password = driver.find_element (By.ID, 'password')
        password.send_keys ('secret_sauc')

        driver.find_element (By.ID, 'login-button').click ()
        time.sleep (2)
        print ('TEST IS OVER')
        driver.quit ()

    def test_select_product(self):
        # ASKING USER
        print ("Приветствую тебя в нашем интернет магазине!")
        print (
            "Выбери один из следующих товаров и укажи его номер: \n1 - Sauce Labs Backpack \n2 - Sauce Labs Bike Light \n3 - Sauce Labs Bolt T-Shirt \n4 - Sauce Labs Fleece Jacket \n5 - Sauce Labs Onesie \n6 - Test.allTheThings() T-Shirt (Red)")
        product = input ()

        if product.isdigit () and int (product) >= 7:
            print ("Такого товара нет. Проверьте корректность ввода.")
            sys.exit ()
        print (f"Вы выбрали товар номер: {product}.")

        # OPTIONS
        options = webdriver.ChromeOptions ()
        options.add_experimental_option ('detach', True)

        # SERVICE
        s = Service ()

        # DRIVER
        driver = webdriver.Chrome (options=options, service=s)
        driver.maximize_window ()
        driver.get (url)
        time.sleep (2)

        # LOGIN, PASSWORD AND CLICK LOGIN BUTTON
        username = driver.find_element (By.ID, 'user-name')
        username.send_keys ('standard_user')

        password = driver.find_element (By.ID, 'password')
        password.send_keys ('secret_sauce')

        driver.find_element (By.ID, 'login-button').click ()
        time.sleep (2)

        # FIND AND SELECT PRODUCT
        value_product = driver.find_element (By.XPATH,
                                             f'//div[@class="inventory_item"][{product}]//div[@data-test="inventory-item-name"]')
        value_product = value_product.text
        print (value_product)
        time.sleep (2)

        value_price_product = driver.find_element (By.XPATH,
                                                   f'//div[@class="inventory_item"][{product}]//div[@data-test="inventory-item-price"]')
        value_price_product = value_price_product.text
        print (value_price_product)
        time.sleep (2)

        select_product = driver.find_element (By.XPATH, f'//div[@class="inventory_item"][{product}]//button')
        select_product.click ()
        print ("PRODUCT SELECTED")
        time.sleep (2)

        print ('TEST IS OVER')
        driver.quit ()


test = Test_1 ()
# test.test_successful_authorization()
# test.test_fail_authorization()
test.test_select_product ()
