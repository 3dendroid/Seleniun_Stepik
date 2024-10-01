from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Sample_project.base.base_class import Base


class Payment_page (Base):

    def __init__(self, driver):
        super ().__init__ (driver)
        self.driver = driver

    # LOCATORS
    finish_button = '//button[@id="finish"]'

    # GETTERS
    def get_finish_button(self):
        return WebDriverWait (self.driver, 10).until (EC.element_to_be_clickable ((By.XPATH, self.finish_button)))

    # ACTIONS
    def click_finish_button(self):
        self.get_finish_button ().click ()
        print ("CLICK FINISH BUTTON")

    def payment(self):
        self.get_current_url ()
        self.click_finish_button ()  # finish button (7.9)
