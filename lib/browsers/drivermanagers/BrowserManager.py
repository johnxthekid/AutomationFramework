import sys
from os import path
sys.path.append(path.join(path.dirname(__file__), "..", "..", ".."))

import uuid
from robot.api import logger

from lib.browsers.drivermanagers.ChromeManager import ChromeManager
from lib.browsers.drivermanagers.EdgeManager import EdgeManager
from lib.browsers.drivermanagers.FirefoxManager import FirefoxManager

chrome = "chrome"
edge = "edge"
firefox = "firefox"


class BrowserSetup:
    _driver = None

    @classmethod
    def _init_browser(cls, browser_type, driver_location=None):
        browser_list = {chrome: ChromeManager, edge: EdgeManager, firefox: FirefoxManager}
        # if cls._driver is None:
        _browser = browser_list.get(browser_type, None)
        if _browser is None:
            raise AttributeError(f"incorrect browser type provide: {browser_type}")

        return _browser(driver_location).open_browser()
        # return cls._driver


class BrowserManager:
    __BROWSER_INSTANCES = {}

    def __init__(self):
        logger.info("Browser Manager set")

    @staticmethod
    def open_browser(browser=None, driver_location=None):
        if browser is None:
            raise AttributeError(f"Please specify one of the following browsers to initialize: \n{chrome, edge, firefox}")
        else:
            return BrowserManager.set_browser_instance(browser, driver_location)

    @staticmethod
    def set_browser_instance(browser, driver_location=None):
        browser_instance = BrowserSetup._init_browser(browser, driver_location)
        browser_id = str(uuid.uuid1())
        BrowserManager.__BROWSER_INSTANCES.update({browser_id: browser_instance})
        return browser_id

    @staticmethod
    def delele_browser_instance(browser_id):
        del BrowserManager.__BROWSER_INSTANCES[browser_id]

    @staticmethod
    def get_browser_instance(browser_id):
        logger.info(f"brower id: {browser_id}")
        logger.debug(f"browser list: {BrowserManager.__BROWSER_INSTANCES}")
        browser = BrowserManager.__BROWSER_INSTANCES.get(browser_id, None)
        logger.info(f"Browser instance: {browser}")
        return browser

    def open_page(self, browser_id, url):
        browser = self.get_browser_instance(browser_id)
        browser.get(url)

    def close_browser(self, browser_id):
        browser = self.get_browser_instance(browser_id)
        browser.quit()

    def get_page_title(self, browser_id):
        browser = self.get_browser_instance(browser_id)
        return browser.title


if __name__ == "__main__":
    bm = BrowserManager()
    browser_id = bm.open_browser('chrome')
    bm.open_page(browser_id, "http://blazedemo.com/")
    print(bm.get_page_title(browser_id))




