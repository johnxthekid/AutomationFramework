from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time


class FirefoxManager:

    def __init__(self, driver_location=None):
        self.driver_location = driver_location if driver_location is not None else \
            "C:\\workspace\\axframework\\config\\BrowserDrivers\\geckodriver.exe"

    def open_browser(self):
        return webdriver.Firefox(executable_path=self.driver_location)


if __name__ == "__main__":
    firefox = "C:\\workspace\\axframework\\config\\BrowserDrivers\\geckodriver.exe"

    firefox_binary = FirefoxBinary("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
    # driver = webdriver.Firefox(firefox_binary=firefox_binary, executable_path=firefox)
    driver = webdriver.Firefox(executable_path=firefox)
    time.sleep(6)
    driver.get("http://facebook.com")
    username = driver.find_element_by_id("email")
    password = driver.find_element_by_id("pass")
    username.send_keys("testuser")
    password.send_keys("testnow")
    password.send_keys(Keys.RETURN)
    driver.close()

