from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class EdgeManager:

    def __init__(self, driver_location=None):
        self.driver_location = driver_location if driver_location is not None else\
            "C:\\workspace\\axframework\\config\\BrowserDrivers\\microsoftWebDriver.exe"

    def open_browser(self):
        '''Need Chrome driver in the ENV PATH'''
        return webdriver.Edge()


if __name__ == "__main__":
    edge = "C:\\workspace\\axframework\\config\\BrowserDrivers\\microsoftWebDriver.exe"
    '''Requires the latest version of Windows 10 to run without driver location'''
    driver = webdriver.Edge()
    time.sleep(6)
    driver.get("http://facebook.com")
    username = driver.find_element_by_id("email")
    password = driver.find_element_by_id("pass")
    username.send_keys("testuser")
    password.send_keys("testnow")
    password.send_keys(Keys.RETURN)
    driver.close()
