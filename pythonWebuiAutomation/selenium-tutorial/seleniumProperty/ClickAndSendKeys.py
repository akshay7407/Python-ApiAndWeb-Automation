from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():

    def sendKeyTest(self):
        baseUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(60)

        # loginLink = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        # loginLink.click()

        emailField = driver.find_element(By.NAME, "username")
        emailField.send_keys("Admin")

        passwordField = driver.find_element(By.NAME, "password")
        passwordField.send_keys("admin123")

        time.sleep(3)

        loginButton = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        loginButton.click()

ff = ClickAndSendKeys()
ff.sendKeyTest()