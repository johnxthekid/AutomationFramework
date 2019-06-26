from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from lib.browsers.drivermanagers.BrowserElementActions import ElementActions


class DemoMainPage:

    def __init__(self, driver):
        self._driver = driver

    def select_departure_city(self, city):
        departure_city = ElementActions(self._driver, *(By.XPATH, f"//select[@name='fromPort']"))
        Select(departure_city.element).select_by_value(city)

    def select_destination_city(self, city):
        destination_city = ElementActions(self._driver, *(By.XPATH, f"//select[@name='toPort']/option[@value='{city}']"))
        destination_city.element.click()

    def search_for_flights(self):
        ElementActions(self._driver, *(By.XPATH, "//input[@type='submit']")).click()

    def get_flight_results(self):
        flights = ElementActions(self._driver, *(By.XPATH, "//table[@class='table']/tbody/tr"), multiple=True)
        return [flight.text for flight in flights.element]