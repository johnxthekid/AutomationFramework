import sys
from os import path

from selenium.common.exceptions import ErrorInResponseException, NoSuchElementException
sys.path.append(path.join(path.dirname(__file__), "..", "..", "..", ".."))

from robot.api import logger

from lib.browsers.drivermanagers.BrowserManager import BrowserManager
from lib.browsers.drivermanagers.BrowserElementActions import ElementActions
from config.browserproperties.sofi.loginpage_properties import (
    sofi_icon, sofi_logo, login_link, login_page_title, login_page_email,
    login_page_password, login_page_submit, login_page_title_value,
    login_page_error
)


class SofiLoginPage:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    _browser = None

    def __init__(self, browser):
        self._browser = browser

    def verify_sofi_page_loaded(self):
        ElementActions.wait_for_element_to_load(self._browser, sofi_logo)

    def goto_sofi_login_page(self):
        login_button = ElementActions(self._browser, *login_link)
        print(f"log in text: {login_button.get_element_text()}")
        login_button.wait_visible(wait_time=5)
        # login_button.click(wait_time=10)
        self._browser.execute_script(f"document.querySelector(`{login_link[1]}`).click()")
        if not ElementActions.is_element_present(self._browser, login_page_title, wait_time=15):
            raise NoSuchElementException("Login page does not display")
        # login_text = ElementActions(self._browser, *login_page_title)
        # login_text.wait_visible(wait_time=10)
        # assert(login_text.get_element_text() == login_page_title_value), "login page not displayed"

    def login_to_sofi(self, username_value, password_value):
        username = ElementActions(self._browser, *login_page_email)
        password = ElementActions(self._browser, *login_page_password)
        submit = ElementActions(self._browser, *login_page_submit)
        username.set_element_text(username_value)
        password.set_element_text(password_value)
        submit.click()  
        if ElementActions.is_element_present(self._browser, login_page_error):
            raise Exception("Error display on login page")


if __name__ == '__main__':
    # bm = BrowserManager()
    # driver = bm.open_browser('chrome')
    bm = BrowserManager()
    browser_id = bm.open_browser('chrome')
    browser = bm.get_browser_instance(browser_id)
    browser.maximize_window()
    sofi = SofiLoginPage(browser)
    browser.get('http://sofi.com/')
    sofi.verify_sofi_page_loaded()
    sofi.goto_sofi_login_page()
    sofi.login_to_sofi("test@test.com", "tester")
