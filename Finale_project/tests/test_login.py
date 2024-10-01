from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Finale_project.pages.login_page import Login_page


def test_login(set_up, set_group):
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

    # LOGIN, SELECT PRODUCT, MAKE A PURCHASE
    log = Login_page (driver)
    log.authorization ()

    # DRIVER QUIT
    driver.quit ()
