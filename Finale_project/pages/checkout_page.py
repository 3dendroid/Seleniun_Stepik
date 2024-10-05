import time

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
    checkbox = '//span[contains(text(),"Данные получателя указаны верно*")]'
    by_cash = '//label[contains(.,"Наличными или картой при получении")]'
    email = '//input[@placeholder="Введите ваш e-mail"]'
    finale_price = '//span[@class="e1j9birj0 e106ikdt0 css-8hy98m e1gjr6xo0"]'
    order_button = '//button[.="Оформить заказ"]'

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

    def get_checkbox(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.checkbox)))

    def get_email(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.email)))

    def get_by_cash(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.by_cash)))

    def get_finale_price(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.finale_price)))

    def get_order_button(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.order_button)))

    # ACTIONS
    def input_name(self, name):
        self.get_name ().send_keys (name)
        time.sleep (3)

    def input_last_name(self, last_name):
        self.get_last_name ().send_keys (last_name)
        time.sleep (3)

    def input_telephone(self, telephone):
        self.get_telephone ().send_keys (telephone)
        time.sleep (3)

    def click_delivery(self):
        self.get_delivery ().click ()
        time.sleep (3)
        self.get_delivery2 ().click ()
        time.sleep (3)
        self.get_delivery3 ().click ()
        time.sleep (3)

    def click_checkbox(self):
        self.get_checkbox ().click ()
        time.sleep (3)

    def click_by_cash(self):
        self.get_by_cash ().click ()
        time.sleep (3)

    def input_email(self, email):
        self.get_email ().send_keys (email)
        time.sleep (3)

    def click_order_button(self):
        self.get_order_button ().click ()
        time.sleep (3)

    # METHODS
    def confirm_order(self):
        self.input_name ('Test')
        print ("INPUT NAME")
        self.input_last_name ('Testov')
        print ("INPUT LAST NAME")
        self.input_telephone ('1234567890')
        print ("INPUT TELEPHONE")
        self.get_screenshot ()
        self.click_delivery ()
        self.click_by_cash ()
        self.click_checkbox ()
        self.input_email ('test@mail.ru')
        print ("INPUT EMAIL")
        self.assert_final_price ('72 890')
        self.click_order_button ()
        time.sleep (3)
        self.get_screenshot ()
