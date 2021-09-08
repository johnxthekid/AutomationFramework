import sys
from os import path, environ
from time import sleep

from selenium.common.exceptions import ErrorInResponseException, NoSuchCookieException, NoSuchElementException
sys.path.append(path.join(path.dirname(__file__), "..", "..", "..", ".."))

from robot.api import logger

from lib.browsers.drivermanagers.BrowserManager import BrowserManager
from lib.browsers.drivermanagers.BrowserElementActions import ElementActions
from config.browserproperties.sofi.loginpage_properties import (
    sofi_icon, sofi_logo, login_link, login_page_title, login_page_email,
    login_page_password, login_page_submit, login_page_title_value,
    login_page_error, verify_button, verify_input, remember_checkbox
)


class SofiLoginPage:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    browser = None

    def __init__(self, driver):
        self.driver = driver
        self.browser = ElementActions(driver)

    def verify_sofi_page_loaded(self):
        self.browser.wait_for_element_to_load(sofi_logo)

    def goto_sofi_login_page(self):
        login_button = self.browser.get(login_link)
        print(f"log in text: {login_button.get_element_text()}")
        # login_button.wait_visible(wait_time=5)
        # login_button.click(wait_time=10)
        self.driver.execute_script(f"document.querySelector(`{login_link[1]}`).click()")
        if not self.browser.is_element_present(login_page_title):
            raise NoSuchElementException("Login page does not display")
        # login_text = ElementActions(self._browser, *login_page_title)
        # login_text.wait_visible(wait_time=10)
        # assert(login_text.get_element_text() == login_page_title_value), "login page not displayed"

    def login_to_sofi(self, username_value, password_value):
        username = self.browser.get(login_page_email)
        password = self.browser.get(login_page_password)
        submit = self.browser.get(login_page_submit)
        username.set_element_text(username_value)
        password.set_element_text(password_value)
        submit.click(validate=False)  
        assert(not self.browser.is_element_present(login_page_error), "error displays on login page")
        if self.browser.is_element_present(verify_button):
            text_field = self.browser.get(verify_input)
            button = self.browser.get(verify_button)
            checkbox = self.browser.get(remember_checkbox)
            raise NoSuchCookieException("Verify code is needed to log in")


if __name__ == '__main__':
    # bm = BrowserManager()
    # driver = bm.open_browser('chrome')
    user = environ.get('sofi_user')
    pwd = environ.get('sofi_password')
    options = None
    bm = BrowserManager()
    browser_id, driver = bm.open_browser('chrome', new_options=options)
    # browser = bm.get_browser_instance(browser_id)
    driver.maximize_window()
    sofi = SofiLoginPage(driver)
    driver.get('http://sofi.com/')
    sofi.verify_sofi_page_loaded()
    sofi.goto_sofi_login_page()
    sofi.login_to_sofi(user, pwd)
