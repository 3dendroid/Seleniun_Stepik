import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Finale_project.base.base_class import Base


class Main_page (Base):

    def __init__(self, driver):
        super ().__init__ (driver)
        self.driver = driver

    # DATAS
    url = 'https://www.citilink.ru/'

    # LOCATORS
    product = '//a[@href="/catalog/smartfony/"]'
    apple = '//input[@id="apple"]'
    slider = '//div[@class="app-catalog-18f9ifi ee2gm9s0"]//div[@class="rc-slider rc-slider-horizontal"]'

    # GETTERS
    def get_select_smartphones(self):
        return WebDriverWait (self.driver, 10).until (EC.element_to_be_clickable ((By.XPATH, self.product)))

    def get_select_apple(self):
        return WebDriverWait (self.driver, 10).until (EC.element_to_be_clickable ((By.XPATH, self.apple)))

    def get_slider(self):
        return WebDriverWait (self.driver, 10).until (EC.element_to_be_clickable ((By.XPATH, self.slider)))

    # ACTIONS
    def click_select_product(self):
        self.get_select_smartphones ().click ()
        print ("CLICK SELECT SMARTPHONES")

    def click_apple(self):
        self.get_select_apple ().click ()
        print ("CLICK APPLE")

    def slide_left(self):
        actions = ActionChains (self.driver)
        actions.click_and_hold (self.slider).move_by_offset (-60, 0).release ().perform ()
        print ("SLIDE LEFT")

    # METHODS
    def select_smartphones(self):
        self.driver.get (self.url)
        self.click_select_product ()
        self.get_current_url ()
        self.assert_url ('https://www.citilink.ru/catalog/smartfony/')
        time.sleep (3)
        self.get_screenshot ()

    def select_apple(self):
        self.click_apple ()
        time.sleep (3)

    def slide(self):
        self.slide_left ()
        time.sleep (3)
