import time

from selenium import webdriver
import pytest
from pages.home.login_page import LoginPage
import unittest


class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseURL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login("Admin", "admin123")

        result = lp.verifyIcon()
        assert result == True
        driver.quit()
