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
    text = '//span[@class="e1ys5m360 e106ikdt0 css-8hy98m e1gjr6xo0"]'

    # GETTERS
    def get_text(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.text)))

    # METHODS

    def confirm_data(self):
        self.assert_url (self.url)
