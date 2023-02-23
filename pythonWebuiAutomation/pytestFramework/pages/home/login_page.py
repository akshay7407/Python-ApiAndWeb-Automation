from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _username_field = "username"
    _password_field = "password"
    _login_button = "//button[text()=' Login ']"

    def getEmailField(self):
        return self.driver.find_element(By.NAME, self._username_field)

    def getPasswordField(self):
        return self.driver.find_element(By.NAME, self._password_field)

    def getLoginButton(self):
        return self.driver.find_element(By.XPATH, self._login_button)

    def clickLoginLink(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._username_field, locatorType="name")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="name")

    def clickLoginButton(self):
        self.getLoginButton().click()

    def login(self, email, password):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginLink()

    def verifyIcon(self):
        result = self.isElementPresent(locator="//*[text()='My Info']", locatorType="xpath")
        return result
