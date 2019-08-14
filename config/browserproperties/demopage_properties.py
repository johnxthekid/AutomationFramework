from selenium.webdriver.common.by import By

# Select flights page
departure_city = (By.XPATH, "//select[@name='fromPort']")
destination_city_option = None
destination_city = (By.XPATH, "//select[@name='toPort']")  #/option[@value='{destination_city_option}']")
search_flight_button = (By.XPATH, "//input[@type='submit']")

# Flight results page
flight_result_table = (By.XPATH, "//table[@class='table']/tbody/tr")


# list of properties by type
id_selector = (By.ID, "name")
xpath_selector = (By.XPATH, "//name/value")
name_selector = (By.NAME, "name")
link_selector = (By.LINK_TEXT, "Continue")
partial_link_selector = (By.PARTIAL_LINK_TEXT, "Cont")  # css=tag#id
css_selector = (By.CSS_SELECTOR, "input.text")  # css=tag.class
class_selector3 = (By.CLASS_NAME, "input[attribute=value]")  # css=tag[attribute=value]
tag_selector2 = (By.TAG_NAME, "h1")  # css=tag.class
