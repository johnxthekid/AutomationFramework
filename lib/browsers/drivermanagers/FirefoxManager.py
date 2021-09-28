import os, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

root_dir = os.path.join(os.path.dirname(__file__), "..", "..", "..", "config", "BrowserDrivers")


class FirefoxManager:

    def __init__(self, driver_location=None):
        self.driver_location = driver_location if driver_location is not None else \
            f"{os.path.join(root_dir, 'geckodriver.exe')}"

        if not os.path.exists(self.driver_location):
            raise AttributeError(f"Driver path does not exist: {self.driver_location}")

    def open_browser(self):
        return webdriver.Firefox(executable_path=self.driver_location)

