import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from login_page_for_test import Login_page


class Test_4:
    def test_login_users(self):
        print('TEST IS STARTED!')

        # DATAS
        url = 'https://www.saucedemo.com/'

        all_users = {
            'standard_user',
            'locked_out_user',
            'performance_glitch_user',
            'error_user',
            'visual_user'
        }

        password = 'secret_sauce'

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
        login = Login_page(driver)

        for user in all_users:
            driver.get(url)
            login.authorization(user, password)
            time.sleep(3)

        # DRIVER QUIT
        print('TEST IS OVER!')
        driver.quit()


test = Test_4()
test.test_login_users()
