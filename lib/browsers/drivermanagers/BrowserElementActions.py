from time import sleep

from selenium.webdriver.common.actions import mouse_button
from selenium.webdriver.support import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchAttributeException, NoSuchElementException, ElementNotVisibleException, \
    InvalidElementStateException, StaleElementReferenceException, ElementClickInterceptedException, TimeoutException

import logging
log = logging.getLogger(__name__)


class ElementActions:
    browser = None
    element = None
    locator = None

    def __init__(self, browser_driver, element=None, locator=None): #, *locator, multiple=False):
        """
        Customs actions that an element can perform on the application
        :param element_instance:
        """
        self.browser = browser_driver
        self.element = element
        self.locator = locator
        # if len(self.locator) > 2:
        #     raise AttributeError(f"locator expected to contain type and value. {self.locator}{len(self.locator)}")

        # self.get(*locator, multiple)
        # if multiple:
        #     self.element = self.browser.find_elements(*locator)
        # else:
        #     self.element = self.browser.find_element(*locator)

    def get(self, locator, many=False, index=None):
        '''
        returns the instance of the elements found on the page
        '''
        if self.is_element_present(locator): #self.browser.find_elements(*locator)
            print("Initializing element")
            self.wait_for_element_to_load(locator)
            if many:
                new_element = self.browser.find_elements(*locator)
                if index is not None:
                    new_element = new_element[index]
            else:
                new_element = self.browser.find_element(*locator)
                print(f"element created: {new_element}")
        else:
            raise AttributeError(f"element was not found. {locator}")
        return ElementActions(self.browser, new_element, locator)

    def get_sub_element(self, locator, parent=None, many=False, index=None):
        '''
        returns the instance of the elements found on the page
        '''
        if parent is not None:
            self.element = parent
        if self.is_element_present(locator): #self.browser.find_elements(*locator)
            print("Initializing element")
            self.wait_for_element_to_load(locator)
            if many:
                new_element = self.element.find_elements(*locator)
                if index is not None:
                    new_element = new_element[index]
            else:
                new_element = self.element.find_element(*locator)
                print(f"element created: {new_element}")
        else:
            raise AttributeError(f"element was not found. {locator}")
        return ElementActions(self.browser, new_element, locator)

    def reload_element(self):
        """
        Recheck the element with the DOM
        """
        self.element = self.browser.find_element(*self.get_element_locator())

    # @classmethod
    # def set_instance(cls, *locator, many):
    #     if many:
    #         cls.element = cls.browser.find_elements(*locator)
    #     else:
    #         cls.element = cls.browser.find_element(*locator)
    #     # if many:
    #     #     self.element = self.browser.find_elements(*locator)
    #     # else:
    #     #     self.element = self.browser.find_element(*locator)
        
    def wait_for_element_to_load(self, locator, wait_time=10):
        try:
            element = EC.presence_of_element_located(locator)
            WebDriverWait(self.browser, wait_time).until(element)
        except TimeoutException:
            raise TimeoutException(f"Page was not loaded, element: {locator} is not present")

    def is_element_present(self, locator, wait_time=10):
        while(True):
            try:
                self.browser.find_element(*locator)
                return True
            except NoSuchElementException:
                if wait_time == 0:
                    return False
                sleep(wait_time)
                wait_time = wait_time - 1

    def get_element_instance(self):
        """
        :return: the instance of the element.
        """
        return self.element

    def get_element_locator(self):
        """
        :return: the locator of the element
        """
        return self.locator

    def get_element_properties(self):
        """
        :return: list of attributes for the elements
        """
        return self.get_element_instance().get_property('attributes')

    def wait_visible(self, expected_status=True, wait_time=1):
        """
        wait for the element's visibility to match the expected status provided
        :param expected_status: if the element should be visible or not
        :param wait_time: how long to wait for the expected status
        :return: True or False
        """
        try:
            if expected_status:
                log.debug("Waiting for the element to be visible")
                return WebDriverWait(self.browser, wait_time).until(EC.visibility_of(self.element))
            else:
                log.debug("Waiting for the element to NOT be visible")
                return WebDriverWait(self.browser, wait_time).until_not(EC.visibility_of(self.element))
        except TimeoutException:
            TimeoutException(f"Waiting for Element to be {expected_status} failed")
            return False

    def click(self, validate=True, wait_time=3):
        """
        Executes the element's click event if it exist.
        This function will not move the mouse pointer over the element
        :param wait_time: time to wait for the element to be visible before clicking
        :return:
        """
        try:
            # self.wait_visible(wait_time=wait_time)
            if validate:
                WebDriverWait(self.browser, wait_time).until(EC.element_to_be_clickable(self.locator)).click()
            else:
                self.element.click()
        except TimeoutException:
            raise TimeoutException(f"Element: {self.locator} was not clickable in time")

    @property
    def select(self):
        '''
        property to initialize the Select library in Selenium
        :return: Select Object
        '''
        return Select(self.element)

    # def get_status(self):
    #     """
    #     returns the status of the element property
    #     :return: property status of the element
    #     """
    #     try:
    #         return self.element.element_info.element.CurrentItemStatus
    #     except AttributeError:
    #         raise AttributeError("This element does not have the CurrentItemStatus property")

    # def wait_status_equal(self, expected_status, wait_time=1):
    #     """
    #     Waits for the status of the element to the be equal to the expected status
    #     :param expected_status: expected_status of the element
    #     :param wait_time: wait time to wait for the element
    #     :return: True or False
    #     """
    #     for num_try in range(wait_time):
    #         if self.get_status() == expected_status:
    #             return True
    #         sleep(1)
    #     else:
    #         return False

    # def is_visible(self):
    #     """
    #     :return: True or False
    #     """
    #     try:
    #         self.element.is_visible()
    #     except TimeoutError:
    #         raise TimeoutError("Element was not loaded in time")
    #     except ElementNotFoundError:
    #         raise ElementNotFoundError("Element was not found")
    #     except AttributeError:
    #         raise AttributeError("Element does not the click pattern")
    #     except TypeError:
    #         raise TypeError(f"Incorrect Element type provided: {type(self.element)}")

    # def is_enabled(self):
    #     """
    #     :return: True or False
    #     """
    #     try:
    #         return self.element.element_info.enabled
    #     except AttributeError:
    #         raise AttributeError("Element does not have IsEnabled property")

    def get_element_type(self):
        """
        :return: element type
        """
        try:
            return self.element.element_info.element.CurrentItemType
        except AttributeError:
            raise AttributeError("Element does not have the CurrentItemType property")

    def is_selected(self):
        """
        :return: the selection status of the element
        """
        try:
            return self.element.is_selected()
        except Exception:
            log.debug(f"element not displayed. {Exception}")
            return False

    # def is_expanded(self):
    #     """
    #     :return: the expanded status of the element
    #     """
    #     try:
    #         return self.element.is_expanded()
    #     except TimeoutError:
    #         log.debug("element not displayed. TimeoutError")
    #         return False
    #     except ElementNotFoundError:
    #         log.debug("element not found. ElementNotFoundError")
    #         return False
    #     except COMError:
    #         log.debug("element is not available. COMError")
    #     except AttributeError:
    #         raise AttributeError("Element does not have the is_expanded function")

    # def get_toggle_state(self):
    #     """
    #     :return: return toggle state of True or False
    #     """
    #     try:
    #         return self.element.get_toggle_state()
    #     except TimeoutError:
    #         log.debug("element not displayed. TimeoutError")
    #         return False
    #     except ElementNotFoundError:
    #         log.debug("element not found. ElementNotFoundError")
    #         return False
    #     except COMError:
    #         log.debug("element is not available. COMError")
    #     except AttributeError:
    #         raise AttributeError("Element does not have the toggle state function")

    # def toggle(self):
    #     """
    #     :return: True if successful
    #     """
    #     try:
    #         self.element.toggle()
    #         return True
    #     except TimeoutError:
    #         log.debug("element not displayed. TimeoutError")
    #         return False
    #     except ElementNotFoundError:
    #         log.debug("element not found. ElementNotFoundError")
    #         return False
    #     except COMError:
    #         log.debug("element is not available. COMError")
    #     except AttributeError:
    #         raise AttributeError("Element does not have the toggle() function")

    # def expand(self):
    #     """
    #     :return: True if successful
    #     """
    #     try:
    #         self.element.expand()
    #         return True
    #     except TimeoutError:
    #         log.debug("element not displayed. TimeoutError")
    #         return False
    #     except ElementNotFoundError:
    #         log.debug("element not found. ElementNotFoundError")
    #         return False
    #     except COMError:
    #         log.debug("element is not available. COMError")
    #     except AttributeError:
    #         raise AttributeError("Element does not have the expand() function")

    # def collapse(self):
    #     """
    #     :return: True if successful
    #     """
    #     try:
    #         self.element.collapse()
    #         return True
    #     except TimeoutError:
    #         log.debug("element not displayed. TimeoutError")
    #         return False
    #     except ElementNotFoundError:
    #         log.debug("element not found. ElementNotFoundError")
    #         return False
    #     except COMError:
    #         log.debug("element is not available. COMError")
    #     except AttributeError:
    #         raise AttributeError("Element does not have the collapse() function")

    def get_element_text(self, wait_time=1):
        """
        retrieves the text value of the element.
        :param wait_time: wait time to retrieves the value
        :return: the text value
        """
        try:
            # self.wait_visible(True, wait_time)
            # return self.get_element_instance().get_attribute('textContent')
            return self.element.text
        except TimeoutError:
            raise TimeoutError("element not displayed. TimeoutError")
        except AttributeError:
            raise AttributeError("Element does not have the text function")
    
    def set_element_text(self, text_value, wait_time=1):
        """
        sets the text value of the element.
        :param text_value: the text value to input
        :param wait_time: wait time to retrieves the value
        """
        try:
            self.wait_visible(True, wait_time)
            self.element.send_keys(text_value)
        except TimeoutError:
            raise TimeoutError("element not displayed. TimeoutError")
        except AttributeError:
            raise AttributeError("Element does not have the set_text() function")
    #
    # def input_click(self, wait_time=1):
    #     """
    #     Simulates the mouse click by moving the mouse over the element
    #     :param wait_time: wait time for the element to be visible before clicking on it
    #     """
    #     self.element.set_focus()
    #     self.wait_visible(True, wait_time)
    #     while wait_time > 0:
    #         try:
    #             self.element.click_input()
    #             break
    #         except TimeoutError:
    #             if wait_time == 0:
    #                 raise TimeoutError("element not displayed. TimeoutError")
    #             else:
    #                 sleep(1)
    #                 wait_time -= 1
    #         except ElementNotFoundError:
    #             if wait_time == 0:
    #                 raise ElementNotFoundError("element not found. ElementNotFoundError")
    #             else:
    #                 sleep(1)
    #                 wait_time -= 1
    #         except AttributeError:
    #             raise AttributeError("Element does not have the set_text() function")
    #         except TypeError:
    #             raise TypeError("Incorrect type set for the element action class. TypeError")
    #
    # def right_input_click(self, wait_time=1):
    #     """
    #     simulates the mouse right clicking function
    #     :param wait_time: wait time to retrieves the value
    #     """
    #     try:
    #         self.element.set_focus()
    #         self.wait_visible(True, wait_time)
    #         self.element.right_click_input()
    #     except TimeoutError:
    #         raise TimeoutError("element not displayed. TimeoutError")
    #     except ElementNotFoundError:
    #         raise ElementNotFoundError("element not found. ElementNotFoundError")
    #     except AttributeError:
    #         raise AttributeError("Element does not have the set_text() function")
    #     except TypeError:
    #         raise TypeError("Incorrect type set for the element action class. TypeError")
    #
    # def invoke_element(self, wait_time=1):
    #     """
    #     calls the invoke pattern on custom elements to simulate clicking
    #     :param wait_time: wait time to retrieves the value
    #     """
    #     try:
    #         self.wait_visible(True, wait_time)
    #         self.element.invoke()
    #     except TimeoutError:
    #         raise TimeoutError("element not displayed. TimeoutError")
    #     except ElementNotFoundError:
    #         raise ElementNotFoundError("element not found. ElementNotFoundError")
    #     except AttributeError:
    #         raise AttributeError("Element does not have the set_text() function")
    #     except TypeError:
    #         raise TypeError("Incorrect type set for the element action class. TypeError")

    # def mouse_press_element(self, press_left_button=True):
    #     """
    #     simulate pressing the mouse button
    #     :param press_left_button: Determine if the left mouse button should be pressed
    #     :param pressed: if the button should be pressed first
    #     """
    #     self.wait_visible()
    #     AC(self.browser).move_to_element(self.element).perform()

    def mouseover_element(self):
        """
        Hovers the mouse over the element
        """
        self.wait_visible()
        AC(self.browser).move_to_element(self.element).perform()