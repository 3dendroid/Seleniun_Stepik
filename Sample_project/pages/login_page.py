import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Sample_project.base.base_class import Base


class Login_page (Base):
    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super ().__init__ (driver)
        self.driver = driver

    # LOCATORS
    user_name = 'user-name'
    password = 'password'
    login_button = 'login-button'
    main_word = '//span[@class="title"]'

    # GETTERS
    def get_user_name(self):
        return WebDriverWait (self.driver, 10).until (EC.element_to_be_clickable ((By.ID, self.user_name)))

    def get_password(self):
        return WebDriverWait (self.driver, 10).until (EC.element_to_be_clickable ((By.ID, self.password)))

    def get_login_button(self):
        return WebDriverWait (self.driver, 10).until (EC.element_to_be_clickable ((By.ID, self.login_button)))

    def get_main_word(self):
        return WebDriverWait (self.driver, 10).until (EC.presence_of_element_located ((By.XPATH, self.main_word)))

    # ACTIONS
    def input_user_name(self, user_name):
        self.get_user_name ().send_keys (user_name)
        print ("INPUT LOGIN")
        time.sleep (2)

    def input_password(self, password):
        self.get_password ().send_keys (password)
        print ("INPUT PASSWORD")
        time.sleep (2)

    def click_login_button(self):
        self.get_login_button ().click ()
        print ("CLICK LOGIN BUTTON")
        time.sleep (2)

    def authorization(self):
        self.driver.get (self.url)
        self.driver.maximize_window ()
        self.get_current_url ()  # get current url (7.4)
        self.input_user_name ('standard_user')
        self.input_password ('secret_sauce')
        self.click_login_button ()
        self.assert_word (self.get_main_word (), 'Products')  # assert word (7.5)
