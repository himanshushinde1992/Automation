import time

from base.baseclass import BasePage


class loginpage(BasePage):
    # locators

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """ locators of the page"""
    Email = "com.assetpanda:id/LoginEmailAdressET"
    Password = "com.assetpanda:id/LoginPasswordET"
    Login = "com.assetpanda:id/LoginBtn"
    text = "ACCOUNT"
    Logout = "LOGOUT"
    ok = "android:id/button2"
    sso_button = "com.assetpanda:id/ssoRb"
    sso_email = "com.assetpanda:id/loginSSOET"

    """"page Actions"""

    """ this method will be used to enter the username and password"""

    def account_details(self):
        self.enterText("ui-test@assetpanda.com", self.Email, "id")
        self.enterText("panda123", self.Password, "id")
        self.hide_keyboard()

    """ this method will be used to click on login button"""

    def click_login_button(self):
        self.click_Element(self.Login, "id")
        self.log.info("login Successful")

    def click_group(self):
        self.click_Element(self.index, "index")

    def click_ok_button(self):
        self.click_Element(self.ok, "id")

    def ss0_button_click(self):
        self.click_Element(self.sso_button, "id")

    def enter_sso_domain(self):
        self.enterText("himanshu.assetpanda.com", self.sso_email, "id")

    """creating a method for login by reusing the abover methods"""

    def do_login(self):
        self.account_details()
        self.click_login_button()
        time.sleep(20)

    def Iselementpresent(self):
        self.is_displayed(self.ok, "id")




    """creating a method for invalidlogin by reusing the above methods"""

    def invalid_login(self):
        self.enterText("ui-test@assetpanda.com", self.Email, "id")
        self.enterText("panda1234", self.Password, "id")
        self.click_login_button()
        time.sleep(20)
        self.click_ok_button()

    """creating a method for valid sso login by reusing the abover methods"""

    def valid_sso_login(self):
        self.ss0_button_click()
        self.enter_sso_domain()
        self.click_login_button()
        time.sleep(20)
        self.screenshot("sso")


