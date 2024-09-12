import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

all_users = {
    'user_1': 'standard_user',
    'user_2': 'locked_out_user',
    'user_3': 'performance_glitch_user',
    'user_4': 'error_user',
    'user_5': 'visual_user'
}

all_password = {'password': 'secret_sauce'}


class Test_login():
    def __init__(self, driver):
        self.driver = driver

    def startup(self):
        print('TEST IS STARTED!')

        # DATAS
        url = 'https://www.saucedemo.com/'

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

        # DRIVER QUIT
        print('TEST IS OVER!')
        driver.quit()

    def authorization(self):
        # USER_1
        user_name = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'user-name')))
        user_name.send_keys('user_1')
        print("Input Login")
        time.sleep(2)

        # PASSWORD
        password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'password')))
        password.send_keys('password')
        print("Input Password")
        time.sleep(2)

        # LOGIN BUTTON
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'login-button')))
        login_button.click()
        print("Input Login Button")
        time.sleep(2)


if __name__ == "__main__":
    login = Test_login(webdriver)
    login.startup()
    login.authorization(all_users[0], all_password)
