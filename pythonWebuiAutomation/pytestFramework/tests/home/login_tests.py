import time
from lib2to3.pgen2 import driver

from selenium import webdriver
import pytest
from pages.home.login_page import LoginPage
import unittest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.lp.login("Admin", "admin123")
        result = self.lp.verifyIcon()
        assert result == True

    @pytest.mark.run(order=2)
    def test_InvalidLogin(self):
        self.lp.login("Admin", "admin1235")
        result = self.lp.verifyIcon()
        assert result == False