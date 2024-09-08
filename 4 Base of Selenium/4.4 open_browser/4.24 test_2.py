import datetime
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# OPTIONS
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
# options.add_argument('--headless')  # headless mode

# SERVICE
s = Service()

# DRIVER
driver = webdriver.Chrome(options=options, service=s)
driver.maximize_window()
driver.get('https://demoqa.com/date-picker')
time.sleep(2)


def main():
    # CLEAR CALENDAR
    date_input = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")

    for i in range(10):
        date_input.send_keys(Keys.BACKSPACE)

    time.sleep(2)

    # CURRENT DATE
    now_date = datetime.datetime.utcnow()

    # ADD 10 DAYS TO CURRENT DATE
    future_date = now_date + datetime.timedelta(days=10)

    # FORMAT THE FUTURE DATE IN MM/DD/YYYY
    formatted_date = future_date.strftime("%m/%d/%Y")

    # ENTER THE NEW DATE INTO THE INPUT FIELD
    date_input.send_keys(formatted_date)
    print(f"Текущая дата: {now_date.strftime('%m-%d-%Y')}")
    print(f"Дата через 10 дней: {formatted_date}")

    time.sleep(2)

    # QUIT
    driver.quit()


if __name__ == "__main__":
    main()
