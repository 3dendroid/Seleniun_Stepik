from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Project.pages.cart_page import Cart_page
from Project.pages.client_informaton_page import Client_information_page
from Project.pages.login_page import Login_page
from Project.pages.main_page import Main_page


class Test_5:

    def test_buy_product(self):
        print('TEST IS STARTED!')

        # OPTIONS
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])  # clear console (7.3)

        # SERVICE
        s = Service()

        # DRIVER
        driver = webdriver.Chrome(options=options, service=s)

        # LOGIN, PASSWORD AND CLICK LOGIN BUTTON
        print('TEST IS STARTED!')

        login = Login_page(driver)
        login.authorization()
        mp = Main_page(driver)
        mp.select_product()
        mp.get_current_url()
        cp = Cart_page(driver)
        cp.product_confirmation()
        cip = Client_information_page(driver)
        cip.input_information()

        # DRIVER QUIT
        print('TEST IS OVER!')
        driver.quit()
