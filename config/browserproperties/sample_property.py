from selenium.webdriver.common.by import By


# list of properties by type
id_selector = (By.ID, "name")
xpath_selector = (By.XPATH, "//name/value")
name_selector = (By.NAME, "name")
link_selector = (By.LINK_TEXT, "Continue")
partial_link_selector = (By.PARTIAL_LINK_TEXT, "Cont")  # css=tag#id
css_selector = (By.CSS_SELECTOR, "input.text")  # css=tag.class
class_selector3 = (By.CLASS_NAME, "input[attribute=value]")  # css=tag[attribute=value]
tag_selector2 = (By.TAG_NAME, "h1")  # css=tag.class
