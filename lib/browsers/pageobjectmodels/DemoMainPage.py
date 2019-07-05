from selenium.webdriver.common.by import By

from lib.browsers.drivermanagers.BrowserElementActions import ElementActions


class DemoMainPage:

    def __init__(self, driver):
        self._driver = driver

    def select_departure_city(self, city):
        departure_city = ElementActions(self._driver, *(By.XPATH, f"//select[@name='fromPort']"))
        departure_city.select.select_by_value(city)

    def select_destination_city(self, city):
        destination_city = ElementActions(self._driver, *(By.XPATH, f"//select[@name='toPort']/option[@value='{city}']"))
        destination_city.click()

    def search_for_flights(self):
        ElementActions(self._driver, *(By.XPATH, "//input[@type='submit']")).click()

    def get_flight_results(self):
        flights = ElementActions(self._driver, *(By.XPATH, "//table[@class='table']/tbody/tr"), multiple=True)
        return [flight.text for flight in flights.element]


if __name__ == '__main__':
    pass
    # bm = BrowserManager('chrome')
    # driver = bm.get_browser_instance()
    # bm.open_page("http://blazedemo.com/")
    # print(bm.get_page_title())
    #
    # demo = DemoMainPage(driver)
    # demo.select_departure_city('Paris')
    # demo.select_destination_city('London')
    # demo.search_for_flights()
    # print(demo.get_flight_results())
    # bm.close_browser()

