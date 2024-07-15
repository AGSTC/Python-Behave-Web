from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import Logger
from behave import *
from selenium import webdriver

baseURL = ReadConfig.getApplicationURL()
username = ReadConfig.getUsername()
password = ReadConfig.getUserPassword()

driver = webdriver.Chrome()
lp = LoginPage(driver)


@given('user on sign in page amazon')
def test_login(self):
    Logger.log_info("***********************Verifying Login Test****************************")
    driver.get(baseURL)
    lp.clickSignIn()


@when('user enter username')
def test_input_username(self):
    lp.setUserName(username)


@when('user click on continue')
def test_click_continue(self):
    lp.clickLogin()


@when('user enter password')
def test_input_password(self):
    lp.setPassword(password)


@when('click on Sign-In')
def test_click_signin(self):
    lp.clickContinue()


@then('verify username on home page')
def test_verify_username(self):
    act_username = lp.verifyUsername()
    if act_username == "Hello, chintan":

        Logger.log_info("***********************Verifying Login Test Passed****************************")
        assert True
    else:
        Logger.log_info("***********************Verifying Login Test Failed****************************")
        assert False


@then('close browser')
def close_browser(self):
    driver.close()

