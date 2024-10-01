from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Finale_project.pages.cart_page import Cart_page
from Finale_project.pages.client_informaton_page import Client_information_page
from Finale_project.pages.finish_page import Finish_page
from Finale_project.pages.login_page import Login_page
from Finale_project.pages.main_page import Main_page
from Finale_project.pages.payment_page import Payment_page


# @pytest.mark.order(3)
def test_buy_product_1(set_up, set_group):
    # for running specific test print in terminal: python -m pytest -svk test.py
    # OPTIONS
    options = webdriver.ChromeOptions ()
    options.add_experimental_option ('detach', True)
    options.add_experimental_option ('excludeSwitches', ['enable-logging'])  # clear console (7.3)

    # SERVICE
    s = Service ()

    # DRIVER
    driver = webdriver.Chrome (options=options, service=s)

    # LOGIN, PASSWORD AND CLICK LOGIN BUTTON
    print ('TEST 1 IS STARTED!')  # some tests (7.11)

    login = Login_page (driver)
    login.authorization ()

    mp = Main_page (driver)
    mp.select_product_1 ()
    mp.get_current_url ()

    cp = Cart_page (driver)
    cp.product_confirmation ()

    cip = Client_information_page (driver)
    cip.input_information ()

    pp = Payment_page (driver)
    pp.payment ()

    f = Finish_page (driver)
    f.get_screenshot ()

    # DRIVER QUIT
    print ('TEST 1 IS OVER!')
    driver.quit ()


# @pytest.mark.order(1)
def test_buy_product_2(set_up, set_group):  # some tests (7.11)
    # OPTIONS
    options = webdriver.ChromeOptions ()
    options.add_experimental_option ('detach', True)
    options.add_experimental_option ('excludeSwitches', ['enable-logging'])  # clear console (7.3)

    # SERVICE
    s = Service ()

    # DRIVER
    driver = webdriver.Chrome (options=options, service=s)

    # LOGIN, PASSWORD AND CLICK LOGIN BUTTON
    print ('TEST 2 IS STARTED!')

    login = Login_page (driver)
    login.authorization ()

    mp = Main_page (driver)
    mp.select_product_2 ()
    mp.get_current_url ()

    cp = Cart_page (driver)
    cp.product_confirmation ()

    # DRIVER QUIT
    print ('TEST 2 IS OVER!')
    driver.quit ()


# @pytest.mark.order(2)
def test_buy_product_3(set_up, set_group):  # some tests (7.11)
    # OPTIONS
    options = webdriver.ChromeOptions ()
    options.add_experimental_option ('detach', True)
    options.add_experimental_option ('excludeSwitches', ['enable-logging'])  # clear console (7.3)

    # SERVICE
    s = Service ()

    # DRIVER
    driver = webdriver.Chrome (options=options, service=s)

    # LOGIN, PASSWORD AND CLICK LOGIN BUTTON
    print ('TEST 3 IS STARTED!')

    login = Login_page (driver)
    login.authorization ()

    mp = Main_page (driver)
    mp.select_product_3 ()
    mp.get_current_url ()

    cp = Cart_page (driver)
    cp.product_confirmation ()

    # DRIVER QUIT
    print ('TEST 3 IS OVER!')
    driver.quit ()
