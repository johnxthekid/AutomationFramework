from selenium.webdriver.common.by import By

# Select flights page
departure_city = (By.XPATH, "//select[@name='fromPort']")
destination_city_option = None
destination_city = (By.XPATH, "//select[@name='toPort']")
search_flight_button = (By.XPATH, "//input[@type='submit']")

# Flight results page
flight_result_table = (By.XPATH, "//table[@class='table']/tbody/tr")
