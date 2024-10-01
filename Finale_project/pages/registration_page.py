import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Finale_project.base.base_class import Base


class Registration_page (Base):

    def __init__(self, driver):
        super ().__init__ (driver)
        self.driver = driver

    # DATAS
    url = 'https://www.citilink.ru/'
    new_login = 'tester456'
    new_password = 'password645'
    new_email = 'testemail@example.com'
    new_phone = '1234567892'

    # LOCATORS
    first_name = '//input[@id="first_name"]'
    email = '//input[@id="email"]'
    password = '//input[@id="reg_password"]'
    phone = '//input[@id="billing_phone"]'
    register_button = '//button[@id="registration-button"]'
    error = '//div[@class="error error_responce_number"]//div[@class="span"]'
    text_error = 'Извините, этот номер телефона уже используется!'
    text_success = 'Активные заказы'

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

    def get_error(self):
        return WebDriverWait (self.driver, 10).until (EC.element_to_be_clickable ((By.XPATH, self.error)))

    def get_success(self):
        return WebDriverWait (self.driver, 10).until (EC.element_to_be_clickable ((By.XPATH, self.text_success)))

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

    def check_error_message(self):
        if self.get_error ().text == self.text_error:
            print ("ERROR MESSAGE:" + self.get_error ().text)
        else:
            print ("SUCCESS MESSAGE:" + self.get_success ().text)
        time.sleep (2)

    def registration(self):
        self.driver.get (self.url)
        self.driver.maximize_window ()
        self.get_current_url ()  # get current url (7.4)
        self.input_first_name (self.new_login)
        self.input_email (self.new_email)
        self.input_password (self.new_password)
        self.input_phone (self.new_phone)
        self.click_register_button ()
        self.check_error_message ()
        self.get_screenshot ()
        time.sleep (3)
        self.get_screenshot ()
