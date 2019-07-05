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
        if cls._driver is None:
            _browser = browser_list.get(browser_type, None)
            if _browser is None:
                raise AttributeError("incorrect browser type provide")

            cls._driver = _browser(driver_location).open_browser()
        return cls._driver


class BrowserManager:

    def __init__(self, browser, driver_location=None):
        self.browser = BrowserSetup._init_browser(browser, driver_location)

    def get_browser_instance(self):
        return self.browser

    def open_page(self, url):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()

    def get_page_title(self):
        return self.browser.title


if __name__ == "__main__":
    bm = BrowserManager('chrome')
    bm.open_page("http://blazedemo.com/")
    print(bm.get_page_title())




