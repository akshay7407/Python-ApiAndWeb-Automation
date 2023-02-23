from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class  CalendarSelection():

    def test1(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(6)

        # Click flights tab
        driver.find_element(By.CSS_SELECTOR, "a[href='?pwaLob=wizard-flight-pwa']").click()
        # Find departing field
        departingField = driver.find_element(By.ID, "d1-btn")
        # Click departing field
        departingField.click()
        # Find the date to be selected
        # Expedia website has changed the DOM after the lecture was made
        # Updated new xpath
        dateToSelect = driver.find_element(By.XPATH,
                                           "(//button[@data-day='23'])[1]")
        # Click the date
        dateToSelect.click()

        time.sleep(3)
        driver.quit()


    def test3(self):
            baseUrl = "http://www.expedia.com"
            driver = webdriver.Chrome()
            driver.maximize_window()
            driver.get(baseUrl)
            driver.implicitly_wait(3)

            # Click flights tab
            driver.find_element(By.CSS_SELECTOR, "a[href='?pwaLob=wizard-flight-pwa']").click()
            # Find departing field
            departingField = driver.find_element(By.ID, "d1-btn")
            # Click departing field
            departingField.click()
            # Expedia website has changed the DOM after the lecture was made
            # Updated new xpath
            calMonth = driver.find_element(By.XPATH, "(//div[@class='uitk-date-picker-month'])[1]")
            allValidDates = calMonth.find_elements(By.TAG_NAME, "button")

            time.sleep(2)

            for date in allValidDates:
                if date.get_attribute("data-day") == "15":
                    date.click()
                    print("its clicked on 15")
                    break

ff = CalendarSelection()
ff.test3()