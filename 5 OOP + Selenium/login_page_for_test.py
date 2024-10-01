from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Login_page ():
    def __init__(self, driver):
        self.driver = driver

    def authorization(self, users, passwords):
        # USER
        user_name = WebDriverWait (self.driver, 10).until (EC.element_to_be_clickable ((By.ID, 'user-name')))
        user_name.send_keys (users)
        print ("Input Login")

        # PASSWORD
        password = WebDriverWait (self.driver, 10).until (EC.element_to_be_clickable ((By.ID, 'password')))
        password.send_keys (passwords)
        print ("Input Password")

        # LOGIN BUTTON
        login_button = WebDriverWait (self.driver, 10).until (EC.element_to_be_clickable ((By.ID, 'login-button')))
        login_button.click ()
        print ("Input Login Button")

        # ASSERT LOGIN
        try:
            changed_url = WebDriverWait (self.driver, 10).until (
                EC.url_to_be ('https://www.saucedemo.com/inventory.html'))
            if not changed_url:
                print (f"User: {users}, Login Failed!\n")

            else:
                print (f"User: {users}, Login Success!")

                # LOGOUT BUTTON
                login_burger = WebDriverWait (self.driver, 10).until (
                    EC.element_to_be_clickable ((By.XPATH, "//button[@id='react-burger-menu-btn']")))
                login_burger.click ()
                logout_button = WebDriverWait (self.driver, 10).until (
                    EC.element_to_be_clickable ((By.XPATH, "//a[@id='logout_sidebar_link']")))
                logout_button.click ()
                print ("Input Logout Button.\n")

        except TimeoutException:
            print (f"User: {users}, Login Failed! Timeout reached.\n")
