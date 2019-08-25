import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

root_dir = os.path.join(os.path.dirname(__file__), "..", "..", "..", "config", "BrowserDrivers")


class ChromeManager:

    def __init__(self, driver_location=None):
        self.driver_location = driver_location if driver_location is not None else \
            f"{os.path.join(root_dir, 'chromedriver.exe')}"

        if not os.path.exists(self.driver_location):
            raise AttributeError(f"Driver path does not exist: {self.driver_location}")

    def open_browser(self):
        chrome_options = None
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        return webdriver.Chrome(self.driver_location, chrome_options=chrome_options)


if __name__ == "__main__":
    # chrome = "C:\\workspace\\axframework\\config\\BrowserDrivers\\chromedriver.exe"
    # driver = webdriver.Chrome(chrome)
    driver = ChromeManager().open_browser()
    time.sleep(6)
    driver.get("http://facebook.com")
    username = driver.find_element_by_id("email")
    password = driver.find_element_by_id("pass")
    username.send_keys("testuser")
    password.send_keys("testnow")
    password.send_keys(Keys.RETURN)
    driver.close()

