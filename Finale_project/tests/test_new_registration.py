from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Finale_project.pages.registration_page import Registration_page


def test_register(set_up, set_group):
    # OPTIONS
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # clear console (7.3)

    # SERVICE
    s = Service()

    # DRIVER
    driver = webdriver.Chrome(options=options, service=s)

    # REGISTRATION, SELECT PRODUCT, MAKE A PURCHASE
    reg = Registration_page(driver)
    reg.registration()

    # DRIVER QUIT
    driver.quit()
