from pageObjects.LoginPage import LoginPage
from pageObjects.HomePage import HomePage
from utilities.readProperties import ReadConfig

class Test_002_ItemOrder:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getUserPassword()

    def test_ItemOrder(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.clickSignIn()
        self.lp.setUserName(self.username)
        self.lp.clickLogin()
        self.lp.setPassword(self.password)
        self.lp.clickContinue()
        self.act_username = self.lp.verifyUsername()

        self.hp = HomePage(self.driver)
        self.hp.clickSearch("iphone 13")
        self.hp.findItem("Apple iPhone 13 (256GB) - Pink")
        handles = self.driver.window_handles
        size = len(handles)
        for x in range(size):
            if handles[x] != self.driver.current_window_handle:
                self.driver.switch_to.window(handles[x])

        mainprice = self.hp.getprice("/html/body/div[4]/div[2]/div[3]/div[11]/div[14]/div[1]/div[1]/span[2]/span[2]/span[2]")
        self.hp.addToCart()
        self.driver.implicitly_wait(50)
        self.hp.goToCart()
        handles = self.driver.window_handles
        for x in range(size):
            if handles[x] != self.driver.current_window_handle:
                self.driver.switch_to.window(handles[x])
        self.driver.implicitly_wait(50)
        cartitem = self.hp.getCartItem("Apple iPhone 13 (256GB) - Pink")
        cartprice = self.hp.getprice("//*[@id='sc-item-C5dbf139f-6264-4a03-9f98-312cb122130b']/div[4]/div/div[2]/p/span/span")
        cartprice = str(cartprice)[:-3]
        if cartitem == "Apple iPhone 13 (256GB) - Pink":
            assert True
        else:
            assert False

        if str(cartprice) == str(mainprice):
            assert True
        else:
            assert False
        self.driver.close()
