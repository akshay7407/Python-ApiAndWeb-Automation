from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class LoginTests():

    def test_validLogin(self):
        baseURL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(13)
        driver.get(baseURL)


        emailField = driver.find_element(By.NAME, "username")
        emailField.send_keys("Admin")

        passwordField = driver.find_element(By.NAME, "password")
        passwordField.send_keys("admin123")



        loginButton = driver.find_element(By.XPATH, "//button[text()=' Login ']")
        loginButton.click()

        userIcon = driver.find_element(By.XPATH, "//*[text()='My Info']")
        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login Failed")

ff = LoginTests()
ff.test_validLogin()