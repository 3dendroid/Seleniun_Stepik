import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Finale_project.base.base_class import Base


class Main_page (Base):

    def __init__(self, driver):
        super ().__init__ (driver)
        self.driver = driver

    # DATAS
    url = 'https://www.citilink.ru/'

    # LOCATORS
    product = '//a[@href="/catalog/smartfony/"]'
    slider = '(//div[@role="slider"])[4]'
    min_price = '(//input[@name="input-min"])[2]'
    filter = '//input[@placeholder="Поиск по фильтрам"]'
    apple = '//div[@data-meta-value="APPLE"]//span[@class="e11v1gn60 app-catalog-389ojc elcxude0"]'
    sort_reviews = '//span[contains(text(),"по рейтингу")]'
    fast_view = '(//span[contains(text(),"Быстрый просмотр")])[1]'
    hover_pointer = '(//a[contains(@title,"темная ночь")])[1]'
    add_to_cart = '//div[@class ="css-zg5qvs e1nf37c40"]'
    cart = '//div[@class="css-etfq0g e1tn9ugy0"]//a[.="Перейти в корзину"]'
    price = '//div[@class="css-etfq0g e1tn9ugy0"]//span[contains(text(),"72 890")]'
    configurator = '//span[contains(text(),"Конфигуратор ПК")]'
    city_list = '//button[contains(@class,"ewtpdih0 css-o6fbp8 etyxved0")]'
    input_city = '//input[@placeholder="Введите название города"]'
    search_result = '//div[@class="PopupScrollContainer"]//li[1]'

    # GETTERS
    def get_select_smartphones(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.product)))

    def get_select_apple(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.apple)))

    def get_slider(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.slider)))

    def get_min_price(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.min_price)))

    def get_filter(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.filter)))

    def get_sort_reviews(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.sort_reviews)))

    def get_fast_view(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.fast_view)))

    def get_add_to_cart(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.add_to_cart)))

    def get_hover_pointer(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.hover_pointer)))

    def get_go_to_cart(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.cart)))

    def get_price(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.price)))

    def get_configurator(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.configurator)))

    def get_city_list(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.city_list)))

    def get_input_city(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.input_city)))

    def get_search_result(self):
        return WebDriverWait (self.driver, 20).until (EC.element_to_be_clickable ((By.XPATH, self.search_result)))

    # ACTIONS
    def click_select_product(self):
        self.get_select_smartphones ().click ()
        print ("CLICK SELECT SMARTPHONES")

    def click_apple(self):
        self.get_select_apple ().click ()
        print ("CLICK APPLE CHECKBOX")

    def slide_left(self):
        actions = ActionChains (self.driver)
        actions.click_and_hold (self.get_slider ()).move_by_offset (-100, 0).release ().perform ()
        print ("SLIDE LEFT")

    def input_min_price(self):
        self.get_min_price ().clear ()
        self.get_min_price ().send_keys ("70000")
        self.get_min_price ().send_keys (Keys.ENTER)
        print ("INPUT MIN PRICE")
        time.sleep (3)

    def input_filter(self):
        self.get_filter ().send_keys ("Apple")
        self.get_filter ().send_keys (Keys.ENTER)
        print ("INPUT APPLE IN FILTER")
        time.sleep (3)

    def sorting(self):
        self.get_sort_reviews ().click ()
        time.sleep (3)

    def click_fast_view(self):
        self.get_fast_view ().click ()
        print ("CLICK FAST VIEW")
        time.sleep (3)

    def click_add_to_cart(self):
        self.get_add_to_cart ().click ()
        print ("CLICK ADD TO CART")
        time.sleep (3)

    def go_to_cart(self):
        self.get_go_to_cart ()
        time.sleep (3)

    def go_to_configurator(self):
        self.get_configurator ()
        time.sleep (3)

    def input_new_city(self, city):
        self.get_input_city ().send_keys (city)
        time.sleep (3)

    def click_search_result(self):
        self.get_search_result ().click ()
        time.sleep (3)

    def click_city_list(self):
        self.get_city_list ().click ()
        time.sleep (3)

    # METHODS
    def select_smartphones(self):
        self.driver.get (self.url)
        time.sleep (5)
        self.click_select_product ()
        self.get_current_url ()
        self.assert_url ('https://www.citilink.ru/catalog/smartfony/')
        time.sleep (3)
        self.get_screenshot ()

    def select_apple(self):
        self.input_filter ()
        self.click_apple ()
        time.sleep (3)
        self.get_screenshot ()

    def select_price(self):
        self.input_min_price ()
        self.slide_left ()
        time.sleep (3)
        self.get_screenshot ()

    def sort_by_reviews(self):
        self.sorting ()
        time.sleep (4)
        self.get_screenshot ()

    def view_and_add_to_cart(self):
        hover = ActionChains (self.driver)
        hover.move_to_element (self.get_hover_pointer ()).perform ()
        self.click_fast_view ()
        time.sleep (3)
        self.click_add_to_cart ()
        self.assert_price ('72 990')  # price
        self.assert_name ('Смартфон Apple iPhone 14 128Gb, A2884, темная ночь')  # name of product
        time.sleep (3)
        hover.move_to_element (self.get_go_to_cart ()).perform ()
        hover.click ().perform ()
        time.sleep (3)
        self.get_screenshot ()

    def select_configurator(self):
        self.driver.get (self.url)
        self.refresh_if_500 ()
        hover = ActionChains (self.driver)
        hover.move_to_element (self.get_configurator ()).click ().perform ()
        self.get_screenshot ()

    def select_city(self, city):
        self.driver.get (self.url)
        self.scroll_to_bottom ()
        self.click_city_list ()
        time.sleep (5)
        self.input_new_city (city)
        time.sleep (5)
        self.click_search_result ()
        time.sleep (5)
        self.get_screenshot ()
