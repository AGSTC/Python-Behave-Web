from selenium.webdriver.common.by import By


class HomePage:
    textbox_search_id = "twotabsearchtextbox"
    button_search_id = "nav-search-submit-button"
    button_addToCart_xpath = "//input[@id='add-to-cart-button']"
    # button_gotoCart_xpath =
    def __init__(self,driver):
        self.driver = driver

    def clickSearch(self,text):
        self.driver.find_element('id', self.textbox_search_id).send_keys(text)
        self.driver.find_element('id', self.button_search_id).click()

    def findItem(self, itemname):
        self.driver.find_element(
            By.PARTIAL_LINK_TEXT,
            itemname,
        ).click()

    def addToCart(self):
        self.driver.find_element(By.XPATH, self.button_addToCart_xpath).click()

    def goToCart(self):
        self.driver.find_element(By.XPATH, "// *[ @ id = 'attach-sidesheet-view-cart-button'] / span / input").click()

    def getCartItem(self,itemname):
        cartitem = self.driver.find_element(
            By.PARTIAL_LINK_TEXT,
            itemname,
        ).text
        return cartitem

    def getprice(self, path):
        price = self.driver.find_element(By.XPATH, path).text
        return price
