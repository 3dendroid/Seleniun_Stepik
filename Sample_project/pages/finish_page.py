from Sample_project.base.base_class import Base


class Finish_page (Base):

    def __init__(self, driver):
        super ().__init__ (driver)
        self.driver = driver

    # LOCATORS

    # GETTERS

    # ACTIONS

    def finish(self):
        self.get_current_url ()
        self.assert_url ('https://www.saucedemo.com/checkout-complete.html')
        self.get_screenshot ()  # get screenshot (7.9)
