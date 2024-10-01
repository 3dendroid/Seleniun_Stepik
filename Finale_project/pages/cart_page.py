from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Finale_project.base.base_class import Base


class Cart_page (Base):

    def __init__(self, driver):
        super ().__init__ (driver)
        self.driver = driver

    # LOCATORS
    checkout_button = '//button[@id="checkout"]'

    # GETTERS
    def get_checkout_button(self):
        return WebDriverWait (self.driver, 10).until (EC.element_to_be_clickable ((By.XPATH, self.checkout_button)))

    # ACTIONS
    def click_checkout_button(self):
        self.get_checkout_button ().click ()
        print ("CLICK CHECKOUT BUTTON")

    def product_confirmation(self):
        self.click_checkout_button ()  # select product (7.7)
