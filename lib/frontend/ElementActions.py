from _ctypes import COMError
from pywinauto.timings import TimeoutError
from pywinauto.findwindows import ElementNotFoundError
from pywinauto.findbestmatch import MatchError
from pywinauto import mouse

from time import sleep

import logging
log = logging.getLogger(__name__)


class ElementActions:

    def __init__(self, element_instance):
        """
        Customs actions that an element can perform on the application
        :param element_instance:
        """
        self.element = element_instance

    def get_element_instance(self):
        """
        :return: the instance of the element.
        """
        return self.element

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
                self.element.wait('visible', wait_time)
                return True
            else:
                log.debug("Waiting for the element to NOT be visible")
                self.element.wait_not('visible', wait_time)
                return True
        except TimeoutError:
            log.debug("element timed out while waiting for the expected visibility status")
            return False
        except ElementNotFoundError:
            log.debug("element was not found while waiting for the expected visibility status")
            return False
        except COMError:
            log.debug("element was inaccessible while waiting for the expected visibility status")
            return False
        except AttributeError:
            raise AttributeError("element does not have the wait function")
        except Exception:
            log.debug("element error thrown")
            return False

    def element_wait(self, property, wait_time=1):
        """
        waits for the status of the element
        'enabled', 'visible', 'exists'
        :param status: property to be validated
        :param wait_time: time to wait for the status
        :return: True or False
        """
        try:
            self.element.wait(property, wait_time)
        except TimeoutError:
            raise TimeoutError("Element was not loaded in time")
        except ElementNotFoundError:
            raise ElementNotFoundError("Element was not found")
        except AttributeError:
            raise AttributeError("Element does not the specify wait property")
        except TypeError:
            raise TypeError(f"Incorrect property type provided: {type(self.element)}")

    def click(self, wait_time=None):
        """
        Executes the element's click event if it exist.
        This function will not move the mouse pointer over the element
        :param wait_time: time to wait for the element to be visible before clicking
        :return:
        """
        if not self.wait_visible(True, wait_time):
            log.debug("Element was not visible before executing the click event")

        try:
            log.debug(f"Executing the click event for the element: {self.element.texts()[0]}")
            self.element.click()
        except TimeoutError:
            raise TimeoutError("Element was not loaded in time")
        except ElementNotFoundError:
            raise ElementNotFoundError("Element was not found")
        except AttributeError:
            raise AttributeError("Element does not the click pattern")
        except TypeError:
            raise TypeError(f"Incorrect Element type provided: {type(self.element)}")

    def get_status(self):
        """
        returns the status of the element property
        :return: property status of the element
        """
        try:
            return self.element.element_info.element.CurrentItemStatus
        except AttributeError:
            raise AttributeError("This element does not have the CurrentItemStatus property")

    def wait_status_equal(self, expected_status, wait_time=1):
        """
        Waits for the status of the element to the be equal to the expected status
        :param expected_status: expected_status of the element
        :param wait_time: wait time to wait for the element
        :return: True or False
        """
        for num_try in range(wait_time):
            if self.get_status() == expected_status:
                return True
            sleep(1)
        else:
            return False

    def is_visible(self):
        """
        :return: True or False
        """
        try:
            self.element.is_visible()
        except TimeoutError:
            raise TimeoutError("Element was not loaded in time")
        except ElementNotFoundError:
            raise ElementNotFoundError("Element was not found")
        except AttributeError:
            raise AttributeError("Element does not the click pattern")
        except TypeError:
            raise TypeError(f"Incorrect Element type provided: {type(self.element)}")

    def is_enabled(self):
        """
        :return: True or False
        """
        try:
            return self.element.element_info.enabled
        except AttributeError:
            raise AttributeError("Element does not have IsEnabled property")

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
        except TimeoutError:
            log.debug("element not displayed. TimeoutError")
            return False
        except ElementNotFoundError:
            log.debug("element not found. ElementNotFoundError")
            return False
        except COMError:
            log.debug("element is not available. COMError")
        except AttributeError:
            raise AttributeError("Element does not have the is_selected function")

    def is_expanded(self):
        """
        :return: the expanded status of the element
        """
        try:
            return self.element.is_expanded()
        except TimeoutError:
            log.debug("element not displayed. TimeoutError")
            return False
        except ElementNotFoundError:
            log.debug("element not found. ElementNotFoundError")
            return False
        except COMError:
            log.debug("element is not available. COMError")
        except AttributeError:
            raise AttributeError("Element does not have the is_expanded function")

    def get_toggle_state(self):
        """
        :return: return toggle state of True or False
        """
        try:
            return self.element.get_toggle_state()
        except TimeoutError:
            log.debug("element not displayed. TimeoutError")
            return False
        except ElementNotFoundError:
            log.debug("element not found. ElementNotFoundError")
            return False
        except COMError:
            log.debug("element is not available. COMError")
        except AttributeError:
            raise AttributeError("Element does not have the toggle state function")

    def toggle(self):
        """
        :return: True if successful
        """
        try:
            self.element.toggle()
            return True
        except TimeoutError:
            log.debug("element not displayed. TimeoutError")
            return False
        except ElementNotFoundError:
            log.debug("element not found. ElementNotFoundError")
            return False
        except COMError:
            log.debug("element is not available. COMError")
        except AttributeError:
            raise AttributeError("Element does not have the toggle() function")

    def expand(self):
        """
        :return: True if successful
        """
        try:
            self.element.expand()
            return True
        except TimeoutError:
            log.debug("element not displayed. TimeoutError")
            return False
        except ElementNotFoundError:
            log.debug("element not found. ElementNotFoundError")
            return False
        except COMError:
            log.debug("element is not available. COMError")
        except AttributeError:
            raise AttributeError("Element does not have the expand() function")

    def collapse(self):
        """
        :return: True if successful
        """
        try:
            self.element.collapse()
            return True
        except TimeoutError:
            log.debug("element not displayed. TimeoutError")
            return False
        except ElementNotFoundError:
            log.debug("element not found. ElementNotFoundError")
            return False
        except COMError:
            log.debug("element is not available. COMError")
        except AttributeError:
            raise AttributeError("Element does not have the collapse() function")

    def get_element_text(self, wait_time=1):
        """
        retrieves the text value of the element.
        :param wait_time: wait time to retrieves the value
        :return: the text value
        """
        try:
            self.wait_visible(True, wait_time)
            return self.element.texts()[0]
        except TimeoutError:
            raise TimeoutError("element not displayed. TimeoutError")
        except ElementNotFoundError:
            raise ElementNotFoundError("element not found. ElementNotFoundError")
        except AttributeError:
            raise AttributeError("Element does not have the texts() function")

    def set_element_text(self, text_value, wait_time=1):
        """
        sets the text value of the element.
        :param text_value: the text value to input
        :param wait_time: wait time to retrieves the value
        """
        try:
            self.wait_visible(True, wait_time)
            self.element.set_text(text_value)
        except TimeoutError:
            raise TimeoutError("element not displayed. TimeoutError")
        except ElementNotFoundError:
            raise ElementNotFoundError("element not found. ElementNotFoundError")
        except AttributeError:
            raise AttributeError("Element does not have the set_text() function")

    def input_click(self, wait_time=1):
        """
        Simulates the mouse click by moving the mouse over the element
        :param wait_time: wait time for the element to be visible before clicking on it
        """
        self.element.set_focus()
        self.wait_visible(True, wait_time)
        while wait_time > 0:
            try:
                self.element.click_input()
                break
            except TimeoutError:
                if wait_time == 0:
                    raise TimeoutError("element not displayed. TimeoutError")
                else:
                    sleep(1)
                    wait_time -= 1
            except ElementNotFoundError:
                if wait_time == 0:
                    raise ElementNotFoundError("element not found. ElementNotFoundError")
                else:
                    sleep(1)
                    wait_time -= 1
            except AttributeError:
                raise AttributeError("Element does not have the set_text() function")
            except TypeError:
                raise TypeError("Incorrect type set for the element action class. TypeError")

    def right_input_click(self, wait_time=1):
        """
        simulates the mouse right clicking function
        :param wait_time: wait time to retrieves the value
        """
        try:
            self.element.set_focus()
            self.wait_visible(True, wait_time)
            self.element.right_click_input()
        except TimeoutError:
            raise TimeoutError("element not displayed. TimeoutError")
        except ElementNotFoundError:
            raise ElementNotFoundError("element not found. ElementNotFoundError")
        except AttributeError:
            raise AttributeError("Element does not have the set_text() function")
        except TypeError:
            raise TypeError("Incorrect type set for the element action class. TypeError")

    def invoke_element(self, wait_time=1):
        """
        calls the invoke pattern on custom elements to simulate clicking
        :param wait_time: wait time to retrieves the value
        """
        try:
            self.wait_visible(True, wait_time)
            self.element.invoke()
        except TimeoutError:
            raise TimeoutError("element not displayed. TimeoutError")
        except ElementNotFoundError:
            raise ElementNotFoundError("element not found. ElementNotFoundError")
        except AttributeError:
            raise AttributeError("Element does not have the set_text() function")
        except TypeError:
            raise TypeError("Incorrect type set for the element action class. TypeError")

    def mouse_press_element(self, press_left_button=True):
        """
        simulate pressing the mouse button
        :param press_left_button: Determine if the left mouse button should be pressed
        :param pressed: if the button should be pressed first
        """
        try:
            elem_rect = self.element.rectangle()
            elem_center = (elem_rect.mid_point().x, elem_rect.mid_point().y)
            self.element.set_focus()
            mouse.press('left', elem_center) if press_left_button else mouse.press('right', elem_center)
            mouse.release('left', elem_center) if press_left_button else mouse.release('right', elem_center)
        except TimeoutError:
            raise TimeoutError("element not displayed. TimeoutError")
        except ElementNotFoundError:
            raise ElementNotFoundError("element not found. ElementNotFoundError")
        except AttributeError:
            raise AttributeError("Element does not have the set_text() function")
        except TypeError:
            raise TypeError("Incorrect type set for the element action class. TypeError")

    def get_element_midpoint(self):
        """
        :return: element midpoint tuple
        """
        return self.element.rectangle().mid_point()

    def mouseover_element(self):
        """
        Hovers the mouse over the element
        """
        self.element.set_focus()
        mouse.move(self.get_element_midpoint())

    def get_element_parent(self):
        """
        :return: the parent object of the element
        """
        return ElementActions(self.element.parent())