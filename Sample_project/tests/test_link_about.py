from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Sample_project.pages.login_page import Login_page
from Sample_project.pages.main_page import Main_page


def test_link_about():
    print ('TEST IS STARTED!')

    # OPTIONS
    options = webdriver.ChromeOptions ()
    options.add_experimental_option ('detach', True)
    options.add_experimental_option ('excludeSwitches', ['enable-logging'])  # clear console (7.3)

    # SERVICE
    s = Service ()

    # DRIVER
    driver = webdriver.Chrome (options=options, service=s)

    # LOGIN, PASSWORD AND CLICK LOGIN BUTTON
    print ('TEST IS STARTED!')

    login = Login_page (driver)
    login.authorization ()

    mp = Main_page (driver)
    mp.select_menu_about ()

    # DRIVER QUIT
    print ('TEST IS OVER!')
    driver.quit ()
