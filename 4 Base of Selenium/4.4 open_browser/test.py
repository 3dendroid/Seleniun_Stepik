from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# ITEMS
items = {'1': 'Sauce Labs Backpack',
         '2': 'Sauce Labs Bike Light',
         '3': 'Sauce Labs Bolt T-Shirt',
         '4': 'Sauce Labs Fleece Jacket',
         '5': 'Sauce Labs Onesie',
         '6': 'Test.allTheThings() T-Shirt (Red)'}
xpathes = {
    '1': "//*[@id='item_4_title_link']/div",
    '2': "//*[@id='item_0_title_link']/div",
    '3': "//*[@id='item_1_title_link']/div",
    '4': "//*[@id='item_5_title_link']/div",
    '5': "//*[@id='item_2_title_link']/div",
    '6': "//*[@id='item_3_title_link']/div"
}
ids = {'1': 'add-to-cart-sauce-labs-backpack',
       '2': 'add-to-cart-sauce-labs-bike-light',
       '3': 'add-to-cart-sauce-labs-bolt-t-shirt',
       '4': 'add-to-cart-sauce-labs-fleece-jacket',
       '5': 'add-to-cart-sauce-labs-onesie',
       '6': 'add-to-cart-test.allthethings()-t-shirt-(red)'
       }

cart_xpathes = {'1': 'item_4_title_link',
                '2': 'item_0_title_link',
                '3': 'item_1_title_link',
                '4': 'item_5_title_link',
                '5': 'item_2_title_link',
                '6': 'item_3_title_link'
                }

# ELEMENTS
login_standard_user = 'standard_user'
password_all = 'secret_sauce'

print("Приветствую тебя в нашем интернет магазине")
print(
    "Выбери один из следующих товаров и укажи его номер: 1 - Sauce Labs Backpack, 2 - Sauce Labs Bike Light, 3 - Sauce Labs Onesie, 4 - Test.allTheThings() T-Shirt, 5 - Fleece Jacket, 6 - Brown T-Shirt")
product = input()
if product in items:
    choice = items[product]
    print(f"Вы выбрали {items[product]}. Товар будет куплен.")
else:
    print("Такого товара нет.")


def main():
    # OPTIONS
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    # options.add_argument('--headless')  # headless mode

    # SERVICE
    s = Service()

    # DRIVER
    driver = webdriver.Chrome(options=options, service=s)
    driver.maximize_window()
    driver.get('https://www.saucedemo.com/')

    # INPUT LOGIN AND PASSWORD
    username = driver.find_element(By.ID, 'user-name')  # by ID attribute
    username.send_keys(login_standard_user)
    print("Input Login")

    password = driver.find_element(By.XPATH, '//*[@id="password"]')  # by XPATH attribute
    password.send_keys(password_all)
    print("Input Password")
    password.send_keys(Keys.ENTER)

    # FIND, SELECT, ADD TO CART
    if product in xpathes:
        xpath = xpathes[product]
        value_product = driver.find_element(By.XPATH, xpath)
        value_product = value_product.text
        print(value_product)
        value_price_product = driver.find_element(By.XPATH,
                                                  "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
        value_price_product = value_price_product.text
        print(value_price_product)

    if product in ids:
        id = ids[product]
        select_product = driver.find_element(By.XPATH, f"//button[@id='{id}']")
        select_product.click()
        print("Select product")

    # CART INFO, CHECK VALUE AND PRICE
    cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    cart.click()
    print("Enter cart")

    if product in cart_xpathes:
        cart_id = cart_xpathes[product]
        cart_xpath = f"//*[@id='{cart_id}']/div"
        cart_value_product = driver.find_element(By.XPATH, cart_xpath)
        cart_value_product = cart_value_product.text
        print(cart_value_product)

    assert value_product == cart_value_product
    print("CART VALUE INFO IS GOOD")
    cart_price_product = driver.find_element(By.XPATH,
                                             "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")
    cart_price_product = cart_price_product.text
    new_cart_price_product = cart_price_product
    print(cart_price_product)

    assert value_price_product == cart_price_product
    print("CART PRICE INFO IS GOOD")

    # CHECKOUT, INPUT DATA
    checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
    checkout.click()
    print("Click checkout")

    first_name = driver.find_element(By.XPATH, "//*[@id='first-name']")
    first_name.send_keys('Denis')
    print("Input first name")

    last_name = driver.find_element(By.XPATH, "//*[@id='last-name']")
    last_name.send_keys('Sazonov')
    print("Input last name")

    postal_code = driver.find_element(By.XPATH, "//*[@id='postal-code']")
    postal_code.send_keys('100500')
    print("Input ZIP")

    continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
    continue_button.click()

    # CART INFO, CHECK VALUE AND PRICE
    finish_value_product = driver.find_element(By.XPATH, xpath)
    finish_value_product = finish_value_product.text
    print(finish_value_product)
    assert value_product == finish_value_product
    print("FINAL VALUE INFO IS GOOD")

    # QUIT
    driver.quit()


if __name__ == "__main__":
    main()
