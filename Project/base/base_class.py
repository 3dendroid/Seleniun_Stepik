class Base:
    """Init driver class"""

    def __init__(self, driver):
        self.driver = driver

    """Method current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("CURRENT URL: " + get_url)

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("GOOD VALUE WORD")
