from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AutoSuggestion:
    def autoCompleteMethod(self):
        baseUrl = "https://www.goibibo.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(20)
        partialText = "Del"
        textToSelect = "Delhi, India(DEL)"

        textElement = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        textElement.send_keys(partialText)

        ulElement = driver.find_element(By.ID, "react-autosuggest-1")
        inner_html = ulElement.get_attribute("innerHTML")
        # print(inner_html)

        liElements = ulElement.find_elements(By.TAG_NAME, "li")
        time.sleep(2)

        for element in liElements:
            if textToSelect in element.text:
                element.click()
                break

        time.sleep(4)

        driver.quit()

at=AutoSuggestion()
at.autoCompleteMethod()