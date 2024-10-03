from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Finale_project.base.base_class import Base


class Checkout_page (Base):

    def __init__(self, driver):
        super ().__init__ (driver)
        self.driver = driver

    # DATAS
    url = 'https://www.citilink.ru/order/checkout/'

    # LOCATORS
    name = '//input[@placeholder="Введите ваше имя"]'
    last_name = '//input[@placeholder="Введите вашу фамилию"]'
    telephone = '//input[@name="contact-form_phone"]'
    delivery = '//label[@class="el7jmaq0 e1twwlg30 css-a8cl06 e1amf8g0"]'
    delivery2 = '//span[contains(text(),"Выбрать пункт самовывоза")]'
    delivery3 = '//button[.="Выбрать"]'
    by_cash = '//label[@class="eddme6n0 e1twwlg30 css-12s80nb e1amf8g0"]'
    checkbox = '//input[@id="contactPaymentConfirm"]'
    email = '//input[@placeholder="Введите ваш e-mail"]'
    finale_price = '//span[@class="e1j9birj0 e106ikdt0 css-8hy98m e1gjr6xo0"]'

    # GETTERS

    def get_name(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.name)))

    def get_last_name(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.last_name)))

    def get_telephone(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.telephone)))

    def get_delivery(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.delivery)))

    def get_delivery2(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.delivery2)))

    def get_delivery3(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.delivery3)))

    def get_by_cash(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.by_cash)))

    def get_checkbox(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.checkbox)))

    def get_email(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.email)))

    def get_finale_price(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.finale_price)))

    # METHODS

    def input_name(self):
        self.get_name ().send_keys ('Ivan')

    def input_last_name(self):
        self.get_last_name ().send_keys ('Ivanov')

    def input_telephone(self):
        self.get_telephone ().send_keys ('89999999999')

    def select_delivery(self):
        self.get_delivery ().click ()
        self.get_delivery2 ().click ()
        self.get_delivery3 ().click ()

    def select_by_cash(self):
        self.get_by_cash ().click ()

    def input_email(self):
        self.get_email ().send_keys ('a@a.ru')

    def input_checkbox(self):
        self.get_checkbox ().click ()

    def confirm_data(self):
        self.assert_price ('71 690')
