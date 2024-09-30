from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
options.add_argument(f"--window-size=1366,768")
options.add_argument(
    f'--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument('--ignore-certificate-errors')
options.add_argument("--password-store=basic")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-extensions")
options.add_argument("--enable-automation")
options.add_argument("--disable-browser-side-navigation")
options.add_argument("--disable-web-security")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-infobars")
options.add_argument("--disable-gpu")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--disable-software-rasterizer")

options.add_argument(f"--user-data-dir=PATH_TO_CHROME_PROFILE")
options.add_argument('--proxy-server=IP_ADRESS:PORT')