from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Finale_project.pages.login_page import Login_page
from Finale_project.pages.main_page import Main_page


def test_register():
    print('TEST IS STARTED!')

    # OPTIONS
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # clear console (7.3)

    # SERVICE
    s = Service()

    # DRIVER
    driver = webdriver.Chrome(options=options, service=s)

    # LOGIN, PASSWORD AND CLICK LOGIN BUTTON
    print('TEST IS STARTED!')

    reg = Reste

    # DRIVER QUIT
    print('TEST IS OVER!')
    driver.quit()
