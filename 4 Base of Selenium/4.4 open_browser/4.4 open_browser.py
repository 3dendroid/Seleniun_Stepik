import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Options
options = webdriver.ChromeOptions ()
# options.add_argument("--start-maximized")
options.add_experimental_option ("detach", True)
options.add_argument ("--disable-infobars")
options.add_experimental_option ("detach", True)
options.add_argument (f"--window-size=1366,768")
options.add_argument (
    f'--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36')
options.add_argument ('--disable-blink-features=AutomationControlled')
options.add_argument ("--disable-extensions")
options.add_argument ("--proxy-server='direct://'")
options.add_argument ("--proxy-bypass-list=*")
options.add_argument ('--ignore-certificate-errors')
options.add_argument ("--password-store=basic")
options.add_argument ("--no-sandbox")
options.add_argument ("--disable-dev-shm-usage")
options.add_argument ("--disable-extensions")
options.add_argument ("--enable-automation")
options.add_argument ("--disable-browser-side-navigation")
options.add_argument ("--disable-web-security")
options.add_argument ("--disable-dev-shm-usage")
options.add_argument ("--disable-gpu")
options.add_argument ("--disable-setuid-sandbox")
options.add_argument ("--disable-software-rasterizer")

# Service
s = Service ()

# Driver
driver = webdriver.Chrome (options=options, service=s)
driver.maximize_window ()
driver.get ('https://www.saucedemo.com/')
# driver.get ('https://www.citilink.ru/')
time.sleep (4)

# Quit
driver.quit ()
