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

    """Method assert price"""

    def assert_price(self, price):
        self.price = self.driver.find_element (By.XPATH, "//span[contains(text(),'72 890')]")
        value_price = self.price.text
        assert value_price == price
        print ("GOOD PRICE VALUE")

    """Method assert final price"""

    def assert_final_price(self, price):
        self.price = self.driver.find_element (By.XPATH, "//span[@class='e1j9birj0 e106ikdt0 css-8hy98m e1gjr6xo0']")
        value_price = self.price.text
        assert value_price == price
        print ("GOOD FINAL PRICE VALUE")

    """Method assert name"""

    def assert_name(self, name):
        self.name = self.driver.find_element (By.XPATH,
                                              "//div[contains(text(),'Смартфон Apple iPhone 14 128Gb,  A2884,  темная ночь')]")
        value_name = self.name.text
        assert value_name == name
        print ("GOOD NAME VALUE")

    """Method scroll down on 240 pixels"""

    def scroll_down(self):
        self.driver.execute_script ("window.scrollTo({top: 230, behavior: 'smooth'});")

    """Method scroll down to bottom"""

    def scroll_to_bottom(self):
        self.driver.execute_script ("window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});")

    """Method refresh"""

    def refresh(self):
        self.driver.refresh ()

    """Method to get title of the page"""

    def get_title(self):
        return self.driver.title

    """Method to refresh page if error 500"""

    def refresh_if_500(self, max_attempts=5):
        attempts = 0
        while attempts < max_attempts:
            if self.get_title () == '500':
                self.refresh ()
                attempts += 1
            else:
                break
        if attempts == max_attempts:
            print ("Exceeded maximum attempts to refresh due to error 500.")
