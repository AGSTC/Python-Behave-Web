class LoginPage:
    link_signin_id = "nav-link-accountList-nav-line-1"
    textbox_username_id = "ap_email"
    button_continue_id = "continue"
    textbox_password_id = "ap_password"
    button_Signin_id = "signInSubmit"
    link_logout_id = "nav-item-signout"
    text_username_xpath = "/html/body/div[1]/header/div/div[1]/div[3]/div/a[2]/div/span"

    def __init__(self,driver):
        self.driver = driver

    def clickSignIn(self):
        self.driver.find_element('id', self.link_signin_id).click()

    def setUserName(self, username):
        self.driver.find_element("id", self.textbox_username_id).clear()
        self.driver.find_element("id", self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element("id", self.textbox_password_id).clear()
        self.driver.find_element("id", self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element('id', self.button_continue_id).click()

    def clickContinue(self):
        self.driver.find_element('id', self.button_Signin_id).click()

    def clickLogout(self):
        self.driver.find_element('id', self.link_logout_id).click()

    def verifyUsername(self):
        self.username = self.driver.find_element('xpath', self.text_username_xpath).text
        return self.username

