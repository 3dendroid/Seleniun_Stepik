import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Test_4:
    def __init__(self):
        self.driver = webdriver

    def login_users(self):
        print ('TEST IS STARTED!')

        # DATAS
        url = 'https://www.saucedemo.com/'

        user = 'locked_out_user'
        password = 'secret_sauce'

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
        user_name = WebDriverWait (driver, 10).until (EC.element_to_be_clickable ((By.ID, 'user-name')))
        user_name.send_keys (user)
        print ("Input Login")

        # PASSWORD
        passwords = WebDriverWait (driver, 10).until (EC.element_to_be_clickable ((By.ID, 'password')))
        passwords.send_keys (password)
        print ("Input Password")

        # LOGIN BUTTON
        login_button = WebDriverWait (driver, 10).until (EC.element_to_be_clickable ((By.ID, 'login-button')))
        login_button.click ()
        print ("Input Login Button")

        # ASSERT LOGIN BUTTON
        text = "Epic sadface: Sorry, this user has been locked out"
        locked_text = WebDriverWait (driver, 10).until (
            EC.presence_of_element_located ((By.XPATH, '//div[@class="error-message-container error"]')))
        value_locked_text = locked_text.text
        print (value_locked_text)

        if text == value_locked_text:
            print (f"{user} Login Failed!")
        else:
            print (f"{user} Login Success!")

        # LOGOUT BUTTON
        login_burger = WebDriverWait (driver, 10).until (
            EC.element_to_be_clickable ((By.XPATH, "//button[@id='react-burger-menu-btn']")))
        login_burger.click ()
        logout_button = WebDriverWait (driver, 10).until (
            EC.element_to_be_clickable ((By.XPATH, "//a[@id='logout_sidebar_link']")))
        logout_button.click ()
        print ("Input Logout Button")
        print (f"Login {user} Passed!")

        # DRIVER QUIT
        print ('TEST IS OVER!')
        driver.quit ()


test = Test_4 ()
test.login_users ()
