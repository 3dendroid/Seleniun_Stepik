import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Test_1:
    def test_select_product(self):
        print('TEST IS STARTED!')

        # DATAS
        url = 'https://www.saucedemo.com/'
        login = 'user-name'
        password = 'password'

        # OPTIONS
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)

        # SERVICE
        s = Service()

        # DRIVER
        driver = webdriver.Chrome(options=options, service=s)
        driver.maximize_window()
        driver.get(url)
        time.sleep(2)

        # LOGIN, PASSWORD AND CLICK LOGIN BUTTON
        username = driver.find_element(By.ID, login)
        username.send_keys('standard_user')

        password = driver.find_element(By.ID, password)
        password.send_keys('secret_sauce')

        driver.find_element(By.ID, 'login-button').click()
        time.sleep(2)

        # FIND AND SELECT PRODUCT
        select_product = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")))
        select_product.click()
        print('CLICK SELECT PRODUCT')

        enter_shopping_cart = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='shopping_cart_container']")))
        enter_shopping_cart.click()
        print('CLICT ENTER SHOPPING CART')

        success_test = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
        value_success_test = success_test.text
        assert value_success_test == 'Your Cart'

        # DRIVER QUIT
        print('TEST IS OVER!')
        driver.quit()


test = Test_1()
test.test_select_product()
