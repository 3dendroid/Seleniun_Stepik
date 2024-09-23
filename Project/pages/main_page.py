from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Project.base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    select_product_1 = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    cart = '//div[@id="shopping_cart_container"]'

    # GETTERS
    def get_select_product_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    # ACTIONS
    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("CLICK SELECT PRODUCT 1")

    def click_cart(self):
        self.get_cart().click()
        print("CLICK CART")

    def select_product(self):
        self.get_current_url()
        self.click_select_product_1()  # select product (7.6)
        self.click_cart()
