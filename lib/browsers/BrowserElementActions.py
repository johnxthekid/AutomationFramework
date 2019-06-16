class ElementActions:

    def __init__(self, browser, element_instance=None):
        """
        Customs actions that an element can perform on the application
        :param element_instance:
        """
        self.browser = browser
        self.element = element_instance

    def get_element(self, element_locator_type, element_value):
        """
        Returns the element base on the provide property value
        :param element_locator_type: the locator type to use to find the element
        :param element_value: the value of the element
        :return: the located element
        """
        locator_type = {"id": self.browser.find_element_by_id,
                        "name": self.browser.find_element_by_name,
                        "xpath": self.browser.find_element_by_xpath,
                        "css": self.browser.find_element_by_css_selector,
                        "class": self.browser.find_element_by_class_name,
                        "tag": self.browser.find_element_by_tag_name,
                        "link": self.browser.find_element_by_link_text,
                        "partial_link": self.browser.find_element_by_partial_link_text}

        self.element = locator_type[element_locator_type](element_value)
        return self.element

    def get_elements(self, element_locator_type, element_value):
        """
        Returns the element base on the provide property value
        :param element_locator_type: the locator type to use to find the element
        :param element_value: the value of the element
        :return: the located elements
        """
        locator_type = {"name": self.browser.find_elements_by_name,
                        "xpath": self.browser.find_elements_by_xpath,
                        "css": self.browser.find_elements_by_css_selector,
                        "class": self.browser.find_elements_by_class_name,
                        "tag": self.browser.find_elements_by_tag_name,
                        "link": self.browser.find_elements_by_link_text,
                        "partial_link": self.browser.find_elements_by_partial_link_text}

        self.element = locator_type[element_locator_type](element_value)
        return self.element
