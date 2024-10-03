from selenium.webdriver.common.by import By

from Finale_project.base.base_class import Base


class Cart_page (Base):

    def __init__(self, driver):
        super ().__init__ (driver)
        self.driver = driver

    # DATAS
    url = 'https://www.citilink.ru/order/'

    # LOCATORS
    confirm_button = '//span[contains(text(),"Перейти к оформлению")]'
    as_guest = '//span[contains(text(),"Продолжить как гость")]'

    # GETTERS

    def get_confirm_button(self):
        return self.driver.find_element (By.XPATH, self.confirm_button)

    def get_as_guest(self):
        return self.driver.find_element (By.XPATH, self.as_guest)

    # ACTIONS
    def click_confirm_button(self):
        self.get_confirm_button ().click ()

    def click_as_guest(self):
        self.get_as_guest ().click ()

    # METHODS

    def to_check_out(self):
        self.assert_url (self.url)
        self.get_screenshot ()
        self.click_confirm_button ()
        self.click_as_guest ()
