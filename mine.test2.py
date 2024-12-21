from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import datetime
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


file=open("log.txt","w")
#driver=webdriver.Chrome()
option=webdriver.ChromeOptions()
option.add_experimental_option('detach',True)
#option.add_argument("--headless")позже
driver=webdriver.Chrome(options=option)

def set_up():
    driver.get(' https://www.saucedemo.com/')
    driver.maximize_window()
#авторизация
def login():
    logins = ("standard_user","locked_out_user","problem_user","performance_glitch_user","error_user","visual_user")
    print(f"Выбрать логин:{logins}")
    user_name = driver.find_element(By.XPATH,'//*[@id="user-name"]')
    login = input("Введите логин :")
    print(f"введён логин:{login}")
    user_name.send_keys(login)
    user_pass = driver.find_element(By.XPATH,'//*[@id="password"]')
    password="secret_sauce"
    user_pass.send_keys(password)
    login_butt = driver.find_element(By.XPATH,'//*[@id="login-button"]')
    login_butt.click()

def test_control_login():
    correct_url="https://www.saucedemo.com/inventory.html"
    get_url=driver.current_url
    assert correct_url==get_url,"test_control_login is Failed"
    print("Авторизация прошла успешно")

#добавление товаров в корзину
#один товар
def price_one(product_name=['Sauce Labs Backpack','Sauce Labs Bike Light','Sauce Labs Bolt T-Shirt','Sauce Labs Fleece Jacket',\
                         'Sauce Labs Onesie','Test.allTheThings() T-Shirt (Red)']):
    print("Выбрать товар,указать номер:\n")
    for i in range(len(product_name)):
        print(f"{(i+1)}:{product_name[i]}")
    product = input()
    i = int(product)-1
    print(f"Вы выбрали:{product_name[i]}")

    product_locator=f"//*[text()='{product_name[i]}']"
    chosen_product=driver.find_element(By.XPATH,product_locator)
    chosen_product.click()
    print(f"Переход в карточку продукта:{product_name[i]}")

    driver.implicitly_wait(3)
    add_to_cart=driver.find_element(By.ID,"add-to-cart")
    add_to_cart.click()
    print("Товар добавлен в корзину")
    back_price=driver.find_element(By.XPATH,'//*[@id="back-to-products"]')
    back_price.click()
    sleep(2)

# второй товар
def price_two(product_name=['Sauce Labs Backpack', 'Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt',
                            'Sauce Labs Fleece Jacket', \
                            'Sauce Labs Onesie', 'Test.allTheThings() T-Shirt (Red)']):
    print("Выбрать товар,указать номер:\n")
    for j in range(len(product_name)):
        print(f"{(j + 1)}:{product_name[j]}")
    product2 = input()
    j = int(product2) - 1
    print(f"Вы выбрали:{product_name[j]}")

    product_locator2 = f"//*[text()='{product_name[j]}']"
    chosen_product = driver.find_element(By.XPATH, product_locator2)
    chosen_product.click()
    print(f"Переход в карточку продукта:{product_name[j]}")

    driver.implicitly_wait(3)
    add_to_cart = driver.find_element(By.ID, "add-to-cart")
    add_to_cart.click()
    print("Товар добавлен в корзину")
    back_price = driver.find_element(By.XPATH, '//*[@id="back-to-products"]')
    back_price.click()

# Переход в корзину
def basket():
    basket_up = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    basket_up.click()
    correct_url = "https://www.saucedemo.com/cart.html"
    get_url = driver.current_url
    assert correct_url == get_url, "test_basket_redirect is Failed"
    driver.save_screenshot(f"screen\\screenshot_basket_"
                           f"{datetime.datetime.now().strftime("%H.%M.%S-%Y.%m.%d")}.png")
    print("Переход в корзину выполнен корректно")

#переход в чеклист
def check_list():
    checkout=driver.find_element(By.XPATH,'//*[@id="checkout"]')
    checkout.click()
    first_name=driver.find_element(By.XPATH,'//*[@id="first-name"]')
    name = input(f"Ваше имя:")
    print(f"{name}")
    first_name.send_keys(name)
    last_name=driver.find_element(By.XPATH,'//*[@id="last-name"]')
    so_name = input("Ваша фамилия:")
    print(f"{so_name}")
    last_name.send_keys(so_name)
    index=driver.find_element(By.XPATH,'//*[@id="postal-code"]')
    index.send_keys("123")
    continue_up=driver.find_element(By.XPATH,'//*[@id="continue"]')
    continue_up.click()
    total=driver.find_element(By.XPATH,'//*[@id="checkout_summary_container"]/div/div[2]/div[8]').text
    print(f"Переход в чеклист выполнен,{total}")

#проверка перехода в чеклист
def test_control_redirect():
    correct_url="https://www.saucedemo.com/checkout-step-two.html"
    get_url=driver.current_url
    assert correct_url==get_url,"test_control_redirect is Failed"
    print("Переход в чеклист выполнен корректно")


#возврат на страницу регистрации
def final():
    finish_up=driver.find_element(By.XPATH,'//*[@id="finish"]')
    finish_up.click()
    back_home=driver.find_element(By.XPATH,'//*[@id="back-to-products"]')
    back_home.click()
    of_menu=driver.find_element(By.XPATH,'//*[@id="react-burger-menu-btn"]')
    of_menu.click()
    sleep(3)
    in_logout=driver.find_element(By.XPATH,'//*[@id="logout_sidebar_link"]')
    in_logout.click()
    print("Тест бизнес плана пройден возврат на страницу регистрации")

set_up()
login()
test_control_login()
price_one()
price_two()
basket()
check_list()
test_control_redirect()
final()

file.close()

