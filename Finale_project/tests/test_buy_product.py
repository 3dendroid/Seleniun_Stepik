from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Finale_project.pages.cart_page import Cart_page
from Finale_project.pages.main_page import Main_page


# @pytest.mark.order(3)
def test_buy_product(set_up, set_group):
    # For running specific test print in terminal: python -m pytest -svk test.py
    # OPTIONS
    options = webdriver.ChromeOptions ()
    options.add_argument ("--start-maximized")
    options.add_argument ("--disable-infobars")
    options.add_argument ("--disable-gpu")
    options.add_argument ("--disable-setuid-sandbox")
    options.add_argument ("--disable-extensions")
    options.add_argument ('--ignore-certificate-errors')
    options.add_argument ('--disable-blink-features=AutomationControlled')
    options.add_argument ("--password-store=basic")
    options.add_argument ("--enable-automation")
    options.add_argument ("--disable-dev-shm-usage")
    options.add_argument ("--disable-browser-side-navigation")
    options.add_argument ("--no-sandbox")
    options.add_argument ("--disable-web-security")
    options.add_experimental_option ('detach', True)
    options.add_experimental_option ('excludeSwitches', ['enable-logging'])  # clear console (7.3)
    options.add_argument ("--ignore-certificate-errors")
    options.add_argument ("--ignore-ssl-errors")
    options.page_load_strategy = 'eager'

    # SERVICE
    s = Service ()

    # DRIVER
    driver = webdriver.Chrome (options=options, service=s)

    # OPEN, SELECT AND ADD TO CART
    mp = Main_page (driver)
    mp.select_smartphones ()
    mp.select_price ()
    mp.select_apple ()
    mp.sort_by_reviews ()
    mp.view_and_add_to_cart ()

    cp = Cart_page (driver)

    # DRIVER QUIT
    print ('TEST IS OVER!')
    driver.quit ()
