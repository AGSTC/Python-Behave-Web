from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage
from utilities.readProperties import ReadConfig
from selenium import webdriver
from behave import *

baseURL = ReadConfig.getApplicationURL()
username = ReadConfig.getUsername()
password = ReadConfig.getUserPassword()
driver = webdriver.Chrome()
lp = LoginPage(driver)
hp = HomePage(driver)
mainprice = 0


@given('user on home page amazon')
def step_itemOrder(context):
    driver.get(baseURL)
    lp.clickSignIn()
    lp.setUserName(username)
    lp.clickLogin()
    lp.setPassword(password)
    lp.clickContinue()
    act_username = lp.verifyUsername()


@when('user enter itemname in search box')
def step_input_item(context):
    hp.clickSearch("iphone 13")


@when('find searched item')
def step_search_item(context):
    hp.findItem("Apple iPhone 13 (256GB) - Pink")
    handles = driver.window_handles
    size = len(handles)
    for x in range(size):
        if handles[x] != driver.current_window_handle:
            driver.switch_to.window(handles[x])


@when('store item price')
def step_store_item(context):
    global mainprice
    mainprice = hp.getprice("/html/body/div[4]/div[2]/div[3]/div[11]/div[14]/div[1]/div[1]/span[2]/span[2]/span[2]")


@when('click on Add to Cart Button')
def step_click_add_to_cart(context):
    hp.addToCart()
    driver.implicitly_wait(50)


@when('click on Go to Cart')
def step_click_go_to_cart(context):
    hp.goToCart()
    handles = driver.window_handles
    size = len(handles)
    for x in range(size):
        if handles[x] != driver.current_window_handle:
            driver.switch_to.window(handles[x])
    driver.implicitly_wait(50)


@then('verify price on cart page')
def step_verify_price(context):
    cartitem = hp.getCartItem("Apple iPhone 13 (256GB) - Pink")
    cartprice = hp.getprice("/html/body/div[1]/div[2]/div[3]/div[4]/div/div[2]/div[1]/div/form/div[2]/div[3]/div[4]/div/div[2]/p/span/text()")
    cartprice = str(cartprice)[:-3]
    if cartitem == "Apple iPhone 13 (256GB) - Pink":
        assert True
    else:
        assert False

    if str(cartprice) == str(mainprice):
        assert True
    else:
        assert False
    driver.close()
















