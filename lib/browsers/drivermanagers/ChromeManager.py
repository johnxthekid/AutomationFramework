from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class ChromeManager:

    def __init__(self, driver_location=None):
        self.driver_location = driver_location if driver_location is not None else \
            "C:\\workspace\\axframework\\config\\BrowserDrivers\\chromedriver.exe"

    def open_browser(self):
        return webdriver.Chrome(self.driver_location)


if __name__ == "__main__":
    chrome = "C:\\workspace\\axframework\\config\\BrowserDrivers\\chromedriver.exe"
    driver = webdriver.Chrome(chrome)
    time.sleep(6)
    driver.get("http://facebook.com")
    username = driver.find_element_by_id("email")
    password = driver.find_element_by_id("pass")
    username.send_keys("testuser")
    password.send_keys("testnow")
    password.send_keys(Keys.RETURN)
    driver.close()

