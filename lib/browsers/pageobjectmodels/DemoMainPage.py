import sys
from os import path
sys.path.append(path.join(path.dirname(__file__), "..", "..", ".."))

from robot.api import logger

from lib.browsers.drivermanagers.BrowserManager import BrowserManager
from lib.browsers.drivermanagers.BrowserElementActions import ElementActions
from config.browserproperties.demopage_properties import *



class DemoMainPage:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    _browser_manager = None

    def __init__(self, driver):
        self.element = ElementActions(driver)

    # @staticmethod
    # def open_browser(browser):
    #     browser_id = BrowserManager.open_browser(browser)
    #     return browser_id

    def select_departure_city(self, browser_id, city):
        # driver = self._browser_manager.get_browser_instance(browser_id)
        departure_city_field = self.element.get(departure_city)
        departure_city_field.select.select_by_value(city)

    def select_destination_city(self, browser_id, city):
        # driver = self._browser_manager.get_browser_instance(browser_id)
        destination_city_field = self.element.get(destination_city)
        destination_city_field.select.select_by_value(city)

    def search_for_flights(self, browser_id):
        # driver = self._browser_manager.get_browser_instance(browser_id)
        self.element.get(search_flight_button).click()

    def get_flight_results(self, browser_id):
        # driver = self._browser_manager.get_browser_instance(browser_id)
        flights = self.element.get(flight_result_table, many=True)
        return [flight.text for flight in flights.element]

    # def open_page(self, browser_id, url):
    #     driver = self._browser_manager.get_browser_instance(browser_id)
    #     driver.get(url)

    # def get_page_title(self, browser_id):
    #     driver = self._browser_manager.get_browser_instance(browser_id)
    #     return driver.title

    # def close_browser(self, browser_id):
    #     driver = self._browser_manager.get_browser_instance(browser_id)
    #     driver.close()
    #     self._browser_manager.delele_browser_instance(browser_id)


if __name__ == '__main__':
    # pass
    bm = BrowserManager()
    browser_id, driver = bm.open_browser('chrome')
    driver.get("http://blazedemo.com/")
    print(bm.get_page_title(browser_id=browser_id))
    
    demo = DemoMainPage(driver=driver)
    demo.select_departure_city(browser_id, 'Paris')
    demo.select_destination_city(browser_id, 'London')
    demo.search_for_flights(browser_id)
    print(demo.get_flight_results(browser_id))
    bm.close_browser(browser_id)

