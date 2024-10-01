import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Login_page ():
    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login_name, login_password):
        # USERNAME
        user_name = WebDriverWait (self.driver, 10).until (EC.element_to_be_clickable ((By.ID, 'user-name')))
        user_name.send_keys (login_name)
        print ("Input Login")
        time.sleep (2)

        # PASSWORD
        password = WebDriverWait (self.driver, 10).until (EC.element_to_be_clickable ((By.ID, 'password')))
        password.send_keys (login_password)
        print ("Input Password")
        time.sleep (2)

        # LOGIN BUTTON
        login_button = WebDriverWait (self.driver, 10).until (EC.element_to_be_clickable ((By.ID, 'login-button')))
        login_button.click ()
        print ("Input Login Button")
        time.sleep (2)
