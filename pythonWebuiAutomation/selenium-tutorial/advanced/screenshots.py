from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Screenshots():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(13)

        # driver.find_element(By.LINK_TEXT, "Login").click()
        # driver.find_element(By.ID, "user_email").send_keys("abc@email.com")
        # driver.find_element(By.ID, "user_password").send_keys("abc")
        # driver.find_element(By.NAME, "commit").click()
        destinationFileName ="D:\PythonTutorial\pythonProject\selenium-tutorial\Screenshots.png"
        # Mac
        # destinationFileName = "C:\\atomar\\Desktop" -> Windows

        try:
            driver.save_screenshot(destinationFileName)
            print("Screenshot saved to directory --> :: " + destinationFileName)
        except NotADirectoryError:
            print("Not a directory issue")


        driver.quit()

ff = Screenshots()
ff.test()