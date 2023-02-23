from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class HiddenElements():

    def testLetsKodeIt(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(6)

        # Find the state of the text box
        driver.execute_script("window.scrollBy(0, 250);")
        textBoxElement = driver.find_element(By.ID, "displayed-text")
        textBoxState = textBoxElement.is_displayed()  # True if visible, False if hidden
        # Exception if not present in the DOM
        print("Text is visible? " + str(textBoxState))
        time.sleep(2)

        # Click the Hide button
        driver.find_element(By.ID, "hide-textbox").click()
        # Find the state of the text box
        textBoxState1 = textBoxElement.is_displayed()
        print("Text is visible? " + str(textBoxState1))
        time.sleep(2)

        # Added code to scroll up because the element was hiding behind the top navigation menu
        # You will learn about scrolling in future lecture
        driver.execute_script("window.scrollBy(0, -150);")
        # Click the Show button
        driver.find_element(By.ID, "show-textbox").click()
        # Find the state of the text box
        textBoxState2 = textBoxElement.is_displayed()
        print("Text is visible? " + str(textBoxState2))
        time.sleep(2)
        # Browser Close
        driver.quit()


ff = HiddenElements()
ff.testLetsKodeIt()
