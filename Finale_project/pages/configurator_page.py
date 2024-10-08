import re
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Finale_project.base.base_class import Base


class Configurator_page (Base):

    def __init__(self, driver):
        super ().__init__ (driver)
        self.driver = driver

    # DATAS
    url = 'https://www.citilink.ru/configurator/'

    # LOCATORS
    gaming = '//div[contains(text(),"Игровые")]'
    for_home = '//div[contains(text(),"Для дома")]'
    for_office = '//div[contains(text(),"Для офиса")]'
    for_design = '//div[contains(text(),"Для дизайна")]'
    sort = '//div[@id="sorting"]'
    sort_by_popularity = '//span[text()="по популярности"]'
    first = '(//button[@data-label="Подробнее"])[1]'
    all_specs = '//ul[@class="js--configuration-card__component-list configuration-card__component-list"]'
    unfold = '//li[contains(@class,"pseudo")]'
    conf_price = '//span[@class="configuration-card_current-price js--configuration-card_current-price js--configuration-price__sum"]'

    # GETTERS
    def get_gaming(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.gaming)))

    def get_for_home(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.for_home)))

    def get_for_office(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.for_office)))

    def get_for_design(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.for_design)))

    def get_sort(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.sort)))

    def get_by_reviews(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.sort_by_popularity)))

    def get_first(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.first)))

    def get_unfold(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.unfold)))

    def get_conf_price(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.conf_price))).text

    def get_all_specs(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.all_specs))).text

    # ACTIONS
    def click_gaming(self):
        self.get_gaming ().click ()
        time.sleep (5)

    def click_for_home(self):
        self.get_for_home ().click ()
        time.sleep (5)

    def click_for_office(self):
        self.get_for_office ().click ()
        time.sleep (5)

    def click_for_design(self):
        self.get_for_design ().click ()
        time.sleep (3)

    def click_sort(self):
        self.get_sort ().click ()
        time.sleep (5)

    def click_by_popularity(self):
        self.get_by_reviews ().click ()
        time.sleep (5)

    def click_first(self):
        self.get_first ().click ()
        time.sleep (5)

    def click_unfold(self):
        self.get_unfold ().click ()
        time.sleep (5)

    # METHODS
    def select_configuration(self, text):
        if text == '1':
            self.refresh_if_500 ()
            self.click_gaming ()
        elif text == '2':
            self.refresh_if_500 ()
            self.click_for_home ()
        elif text == '3':
            self.refresh_if_500 ()
            self.click_for_office ()
        elif text == '4':
            self.refresh_if_500 ()
            self.click_for_design ()

    def select_by_popularity(self):
        self.refresh_if_500 ()
        self.scroll_down ()
        self.click_sort ()

        self.refresh_if_500 ()
        self.scroll_down ()

        self.refresh_if_500 ()
        self.click_by_popularity ()

        self.refresh_if_500 ()
        self.scroll_down ()

        self.refresh_if_500 ()
        self.click_first ()
        self.scroll_down ()
        self.click_unfold ()
        self.get_screenshot ()

        text = self.get_all_specs ()
        cleaned_text = re.sub (r'Свернуть список компонентов', '', text)
        print ("CONFIGURATION: ", cleaned_text)
        print ("PRICE: ", self.get_conf_price () + " руб.")
        with open (r'C:\Users\GIGACHAD\Documents\3dendroid\Seleniun_Stepik\Finale_project\texts\configuration.txt', 'w',
                   encoding='utf-8') as file:
            file.write (cleaned_text)
