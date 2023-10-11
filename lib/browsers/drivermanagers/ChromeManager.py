import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

root_dir = os.path.join(os.path.dirname(__file__), "..", "..", "..", "config", "BrowserDrivers")


class ChromeManager:

    def __init__(self, driver_location=None, new_options=None):
        self.driver_location = driver_location if driver_location is not None else \
            f"{os.path.join(root_dir, 'chromedriver')}"
        self.new_options = new_options

        if not os.path.exists(self.driver_location):
            raise AttributeError(f"Driver path does not exist: {self.driver_location}")

    def open_browser(self):
        '''
        Opens the chrome browser. Accepts the different options for the
        chrome browser.
        # chrome_options = None
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument('--user-data-dir=C:\selenum\ChromeProfile')
        # --user-data-dir=%localappdata%\\Google\\Chrome\\User Data   --profile-directory=Profile 2
        
        chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\ChromeProfile"
        '''


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# options = webdriver.ChromeOptions()
# service = ChromeService(executable_path=CHROMEDRIVER_PATH)
# driver = webdriver.Chrome(service=service, options=options)


        chrome_options = webdriver.ChromeOptions()
        service = ChromeService(executable_path=self.driver_location)
        if self.new_options is not None:
            for value in self.new_options:
                if isinstance(value, tuple):
                    chrome_options.add_experimental_option(value[0], value[1])
                else:
                    chrome_options.add_argument(value)
        return webdriver.Chrome(service=service, options=chrome_options)

