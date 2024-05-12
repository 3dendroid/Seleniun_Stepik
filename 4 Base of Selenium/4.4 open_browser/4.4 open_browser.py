from selenium import webdriver
from selenium.webdriver.chrome.service import Service


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service()
driver = webdriver.Chrome(options=options, service=s)
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

#code is not working