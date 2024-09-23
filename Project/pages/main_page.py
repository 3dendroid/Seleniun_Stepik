import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Project.base.base_class import Base


class Main_page(Base):
    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    shopping_cart = '//div[@id="shopping_cart_container"]'
    product_1 = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    drop_down_list = '//button[@id="react-burger-menu-btn"]'
    log_out = '//a[@id="logout_sidebar_link"]'

    # GETTERS
    def get_product(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_1)))

    def get_shopping_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.shopping_cart)))

    # ACTIONS

    def click_add_to_cart(self):
        self.get_product().click()
        print("CLICK SELECT PRODUCT 1")
        time.sleep(2)

    def click_shopping_cart(self):
        self.get_shopping_cart().click()
        print("CLICK SHOPPING CART")
        time.sleep(2)

    def select_product(self):
        self.click_add_to_cart()
        self.click_shopping_cart()  # select product (7.6)
