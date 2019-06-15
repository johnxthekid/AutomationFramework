from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class EdgeManager:

    def __init__(self, driver_location=None):
        pass


if __name__ == "__main__":
    edge = "C:\\workspace\\axframework\\config\\BrowserDrivers\\microsoftWebDriver.exe"
    driver = webdriver.Edge(edge)
    time.sleep(6)
    driver.get("http://facebook.com")
    username = driver.find_element_by_id("email")
    password = driver.find_element_by_id("pass")
    username.send_keys("testuser")
    password.send_keys("testnow")
    password.send_keys(Keys.RETURN)
    driver.close()
