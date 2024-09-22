from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Project.pages.login_page import Login_page


class Test_5:

    def test_buy_product(self):
        print('TEST IS STARTED!')

        # OPTIONS
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)

        # SERVICE
        s = Service()

        # DRIVER
        driver = webdriver.Chrome(options=options, service=s)

        # LOGIN, PASSWORD AND CLICK LOGIN BUTTON
        print('TEST IS STARTED!')

        login = Login_page(driver)
        login.authorization()

        # ENTER SHOPPING CART

        select_product = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")))
        select_product.click()
        print('CLICK SELECT PRODUCT')

        enter_shopping_cart = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='shopping_cart_container']")))
        enter_shopping_cart.click()
        print('CLICT ENTER SHOPPING CART')

        # DRIVER QUIT
        print('TEST IS OVER!')
        driver.quit()
