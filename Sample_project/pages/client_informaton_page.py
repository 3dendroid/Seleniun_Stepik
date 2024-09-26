from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Sample_project.base.base_class import Base


class Client_information_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    first_name = '//input[@id="first-name"]'
    last_name = '//input[@id="last-name"]'
    zip_code = '//input[@id="postal-code"]'
    continue_button = '//input[@id="continue"]'

    # GETTERS
    def get_first_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_zip_code(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.zip_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.continue_button)))

    # ACTIONS
    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("INPUT FIRST NAME")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("INPUT LAST NAME")

    def input_zip_code(self, zip_code):
        self.get_zip_code().send_keys(zip_code)
        print("INPUT ZIP CODE")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("CLICK CONTINUE BUTTON")

    def input_information(self):
        self.get_current_url()
        self.input_first_name('DENIS')
        self.input_last_name('SAZONOV')
        self.input_zip_code('100500')
        self.click_continue_button()  # input information (7.8)
