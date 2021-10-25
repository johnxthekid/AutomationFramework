import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

root_dir = os.path.join(os.path.dirname(__file__), "..", "..", "..", "config", "BrowserDrivers")


class EdgeManager:

    def __init__(self, driver_location=None):
        self.driver_location = driver_location if driver_location is not None else \
            f"{os.path.join(root_dir, 'microsoftWebDriver.exe')}"

        if not os.path.exists(self.driver_location):
            raise AttributeError(f"Driver path does not exist: {self.driver_location}")

    def open_browser(self):
        """
        Need Chrome driver in the ENV PATH
        """
        return webdriver.Edge()
