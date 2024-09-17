from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Login_page():
    # DATAS
    users = {
        'standard_user',
        'locked_out_user',
        'performance_glitch_user',
        'error_user',
        'visual_user'
    }

    passwords = {'secret_sauce'}

    def __init__(self, driver):
        self.driver = driver

    def authorization(self, users, passwords):
        # USER
        user_name = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'user-name')))
        user_name.send_keys(users)
        print("Input Login")

        # PASSWORD
        password = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'password')))
        password.send_keys(passwords)
        print("Input Password")

        # LOGIN BUTTON
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'login-button')))
        login_button.click()
        print("Input Login Button")

        # ASSERT LOGIN BUTTON

        text = "Epic sadface: Sorry, this user has been locked out"
        locked_text = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="error-message-container error"]')))
        value_locked_text = locked_text.text
        print(value_locked_text)

        # if text != value_locked_text:
        #     print(f"User {users} Login Success!")
        # else:
        #     print(f"{users} Login Failed!")

        # LOGOUT BUTTON
        login_burger = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='react-burger-menu-btn']")))
        login_burger.click()
        logout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']")))
        logout_button.click()
        print("Input Logout Button")

        # continue
