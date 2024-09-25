from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Project.base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    product_1 = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    product_2 = '//div[normalize-space()="Sauce Labs Bike Light"]'
    product_3 = '//div[normalize-space()="Sauce Labs Bolt T-Shirt"]'
    cart = '//div[@id="shopping_cart_container"]'
    menu = '//button[@id="react-burger-menu-btn"]'
    link_about = '//a[@id="about_sidebar_link"]'

    # GETTERS
    def get_select_product_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_1)))

    def get_select_product_2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_2)))

    def get_select_product_3(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_3)))

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_menu(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_link_about(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.link_about)))

    # ACTIONS
    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("CLICK SELECT PRODUCT 1")

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("CLICK SELECT PRODUCT 2")

    def click_select_product_3(self):
        self.get_select_product_3().click()
        print("CLICK SELECT PRODUCT 3")

    def click_cart(self):
        self.get_cart().click()
        print("CLICK CART")

    def click_menu(self):
        self.get_menu().click()
        print("CLICK MENU")

    def click_link_about(self):
        self.get_link_about().click()
        print("CLICK LINK ABOUT")

    # METHODS
    def select_menu_about(self):
        self.get_current_url()
        self.click_menu()
        self.click_link_about()  # second test (7.10)
        self.assert_url('https://saucelabs.com/')
        self.get_screenshot()

    def select_product_1(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()

    def select_product_2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()

    def select_product_3(self):
        self.get_current_url()
        self.click_select_product_3()  # select product (7.6)
        self.click_cart()
