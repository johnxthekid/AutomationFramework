import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from robot.api import logger

from lib.browsers.drivermanagers.BrowserManager import BrowserManager
from lib.frontend.apphelpers.SampleNotepadHelper import SampleNotepadHelper
from lib.browsers.pageobjectmodels.DemoMainPage import DemoMainPage
from lib.browsers.pageobjectmodels.sofi.sofi_login import SofiLoginPage


class AllKeywordsLibrary(DemoMainPage, SampleNotepadHelper, SofiLoginPage):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    _browser_manager = None
    _browser = None
    _browser_id = None
    _driver = None

    def __init__(self, run_location):
        logger.info(f"Running keyword library: {run_location}")
        self._browser_manager = BrowserManager()

        SampleNotepadHelper.__init__(self)
        
    def open_browser(self, browser_type, options=None):
        self._browser_id, self.driver = BrowserManager.open_browser(browser_type, options)
        self._browser = BrowserManager.get_browser_instance(self._browser_id)
        DemoMainPage.__init__(self, self.driver)
        SofiLoginPage.__init__(self, self.driver)


    def open_page(self, url):
        self.driver.get(url)

    def get_page_title(self):
        return self._browser_manager.get_page_title()

    def close_browser(self):
        self._browser_manager.close_browser(self._browser_id)