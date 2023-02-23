from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Service

class RunChromeTests():

    def test(self):
        service = Service(executable_path="D:\PythonTutorial\pythonProject\selenium-tutorial\drivers\chromedriver.exe")
        # Instantiate Browser
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        # Open the provided URL
        driver.get("https://www.letskodeit.com")

runtests = RunChromeTests()
runtests.test()