from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import Logger


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getUserPassword()

    def test_login(self, setup):
        Logger.log_info("***********************Verifying Login Test****************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.clickSignIn()
        self.lp.setUserName(self.username)
        self.lp.clickLogin()
        self.lp.setPassword(self.password)
        self.lp.clickContinue()
        self.act_username = self.lp.verifyUsername()
        if self.act_username == "Hello, chintan":
            Logger.log_info("***********************Verifying Login Test Passed****************************")
            self.driver.close()
            assert True
        else:
            Logger.log_info("***********************Verifying Login Test Failed****************************")
            self.driver.close()
            assert False
        #
        #
