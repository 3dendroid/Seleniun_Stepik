import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Finale_project.base.base_class import Base


class Registration_page (Base):
    url = 'https://waxashop.ru/signup/'

    def __init__(self, driver):
        super ().__init__ (driver)
        self.driver = driver

    # LOCATORS
    first_name = '//input[@id="first_name"]'
    email = '//input[@id="email"]'
    password = '//input[@id="reg_password"]'
    phone = '//input[@id="billing_phone"]'
    register_button = '//button[@id="registration-button"]'

    # GETTERS
    def get_first_name(self):
        return WebDriverWait (self.driver, 10).until (EC.element_to_be_clickable ((By.XPATH, self.first_name)))

    def get_email(self):
        return WebDriverWait (self.driver, 10).until (EC.element_to_be_clickable ((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait (self.driver, 10).until (EC.element_to_be_clickable ((By.XPATH, self.password)))

    def get_phone(self):
        return WebDriverWait (self.driver, 10).until (EC.element_to_be_clickable ((By.XPATH, self.phone)))

    def get_register_button(self):
        return WebDriverWait (self.driver, 10).until (EC.element_to_be_clickable ((By.XPATH, self.register_button)))

    # ACTIONS
    def input_first_name(self, first_name):
        self.get_first_name ().send_keys (first_name)
        print ("INPUT FIRST NAME")
        time.sleep (2)

    def input_email(self, email):
        self.get_email ().send_keys (email)
        print ("INPUT EMAIL")
        time.sleep (2)

    def input_password(self, password):
        self.get_password ().send_keys (password)
        print ("INPUT PASSWORD")
        time.sleep (2)

    def input_phone(self, email):
        self.get_phone ().send_keys (email)
        print ("INPUT PHONE")
        time.sleep (2)

    def click_register_button(self):
        self.get_register_button ().click ()
        print ("CLICK REGISTER BUTTON")

    def registration(self):
        self.driver.get (self.url)
        self.driver.maximize_window ()
        self.get_current_url ()  # get current url (7.4)
        self.input_first_name ('tester777')
        self.input_email ('testemail@example777.com')
        self.input_password ('password777')
        self.input_phone ('1234567890')
        self.click_register_button ()
        time.sleep (3)
        self.get_screenshot ()
