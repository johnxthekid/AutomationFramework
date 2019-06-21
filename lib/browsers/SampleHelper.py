from . import BrowserElementActions, ChromeManager, EdgeManager, FirefoxManager

chrome = "chrome"
chrome_location = "C:\\workspace\\axframework\\config\\BrowserDrivers\\chromedriver.exe"
edge = "edge"
edge_location = "C:\\workspace\\axframework\\config\\BrowserDrivers\\microsoftWebDriver.exe"
firefox = "firefox"
firefox_location = "C:\\workspace\\axframework\\config\\BrowserDrivers\\geckodriver.exe"


class SampleHelper():
    def __init__(self, browser_type):
        self.browser = self.get_browser(browser_type)

    def get_browser(self, browser_type):
        browser_list = {chrome: ChromeManager, edge: EdgeManager, firefox: FirefoxManager}
        return browser_list[browser_type]()
