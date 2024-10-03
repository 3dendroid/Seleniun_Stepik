import datetime

from selenium.webdriver.common.by import By


class Base:
    """Init driver class"""

    def __init__(self, driver):
        self.driver = driver

    """Method current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print ("CURRENT URL: " + get_url)

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print ("GOOD VALUE WORD")

    """Method screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow ().strftime ("%Y_%m_%d_%H_%M_%S")
        path = 'C:\\Users\\GIGACHAD\\Documents\\3dendroid\\Seleniun_Stepik\\Finale_project\\screenshots\\'
        name_screenshot = 'screenshot_' + now_date + '.png'
        self.driver.save_screenshot (path + name_screenshot)
        print ("SCREENSHOT SAVED")

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print ("GOOD VALUE URL")

    def assert_price(self, price):
        self.price = self.driver.find_element (By.XPATH,
                                               "//span[@class='e1j9birj0 e106ikdt0 css-56qww8 e1gjr6xo0'][normalize-space()='71 690']")
        value_price = self.price.text
        assert value_price == price
        print ("GOOD VALUE PRICE")

    def assert_name(self, name):
        self.name = self.driver.find_element (By.XPATH, "//h4[contains(text(),'Apple iPhone 14 128Gb,')]")
        value_name = self.name.text
        assert value_name == name
        print ("GOOD VALUE NAME")
