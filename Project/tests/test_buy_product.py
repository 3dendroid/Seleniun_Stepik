import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Project.pages.cart_page import Cart_page
from Project.pages.login_page import Login_page
from Project.pages.main_page import Main_page


@pytest.mark.order(3)
def test_buy_product_1():
    # OPTIONS
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # clear console (7.3)

    # SERVICE
    s = Service()

    # DRIVER
    driver = webdriver.Chrome(options=options, service=s)

    # LOGIN, PASSWORD AND CLICK LOGIN BUTTON
    print('TEST 1 IS STARTED!')  # some tests (7.11)

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product_1()
    mp.get_current_url()

    cp = Cart_page(driver)
    cp.product_confirmation()

    # cip = Client_information_page(driver)
    # cip.input_information()
    #
    # pp = Payment_page(driver)
    # pp.payment()
    #
    # f = Finish_page(driver)
    # f.get_screenshot()

    # DRIVER QUIT
    print('TEST 1 IS OVER!')
    driver.quit()


@pytest.mark.order(1)
def test_buy_product_2():  # some tests (7.11)
    # OPTIONS
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # clear console (7.3)

    # SERVICE
    s = Service()

    # DRIVER
    driver = webdriver.Chrome(options=options, service=s)

    # LOGIN, PASSWORD AND CLICK LOGIN BUTTON
    print('TEST 2 IS STARTED!')

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product_2()
    mp.get_current_url()

    cp = Cart_page(driver)
    cp.product_confirmation()

    # DRIVER QUIT
    print('TEST 2 IS OVER!')
    driver.quit()


@pytest.mark.order(2)
def test_buy_product_3():  # some tests (7.11)
    # OPTIONS
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # clear console (7.3)

    # SERVICE
    s = Service()

    # DRIVER
    driver = webdriver.Chrome(options=options, service=s)

    # LOGIN, PASSWORD AND CLICK LOGIN BUTTON
    print('TEST 3 IS STARTED!')

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product_3()
    mp.get_current_url()

    cp = Cart_page(driver)
    cp.product_confirmation()

    # DRIVER QUIT
    print('TEST 3 IS OVER!')
    driver.quit()
