import sys
from os import path

from selenium.common.exceptions import ErrorInResponseException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
sys.path.append(path.join(path.dirname(__file__), "..", "..", "..", ".."))

from robot.api import logger

from lib.browsers.drivermanagers.BrowserManager import BrowserManager
from lib.browsers.drivermanagers.BrowserElementActions import ElementActions
# from config.browserproperties.amazon.loginpage_properties import *
import config.browserproperties.amazon.loginpage_properties as props


class AmazonLoginPage:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    _browser = None
    element = None

    def __init__(self, browser):
        self._browser = browser
        self.element = ElementActions(self._browser)

    def __exit__(self, exception_type, exception_value, traceback):
        # self._browser.quit()
        pass

    def test_get(self):
        self.element.wait_for_element_to_load(props.amazon_logo)
        signin_button = self.element.get(props.amazon_nav_account_menu)
        signin_text = self.element.get(props.amazon_signin_text_field)
        print(f"log in text: {signin_text.get_element_text()}")
        signin_button.click()
        self.element.get(props.amazon_signin_title)

    def verify_amazon_page_loaded(self):
        self.element.wait_for_element_to_load(props.amazon_logo)

    def goto_amazon_signin_page(self):
        signin_button = self.element.get(props.amazon_nav_account_menu)
        signin_text = self.element.get(props.amazon_signin_text_field)
        print(f"log in text: {signin_text.get_element_text()}")
        signin_button.click()
        self.element.get(props.amazon_signin_title)

    def login_to_amazon(self, username_value, password_value):
        username = self.element.get(props.amazon_signin_email)
        continue_button = self.element.get(props.amazon_signin_continue)
        # username_value = input("User email: ")
        username.set_element_text(username_value)
        continue_button.click()
        password = self.element.get(props.amazon_signin_password)
        # password_value = input("password value: ")
        password.set_element_text(password_value)
        submit = self.element.get(props.amazon_signin_button)
        submit.click()  
        self.element.get(props.amazon_nav_account_menu)
        account_button = self.element.get(props.amazon_nav_account_menu)
        user_text = account_button.get_element_text()
        if "Hello, John" not in user_text:
            raise Exception(f"user was not logged, text found:\n {user_text}")

    def goto_amazon_gift_card_page(self):
        my_account = self.element.get(props.amazon_nav_account_menu)
        my_account.click()

        self.element.get(props.amazon_account_title)
        self.element.get(props.amazon_account_giftcard).click()
        self.element.get(props.amazon_giftcard_balance)
        gitfcard_balance = self.element.get(props.amazon_giftcard_balance)
        print(f"current balance: {gitfcard_balance.get_element_text()}")
        giftcard_balance_tab = self.element.get(props.amazon_giftcard_balance_tab)
        giftcard_balance_tab.click()
        assert(giftcard_balance_tab.get_element_text() == "View Gift Card Balance and Activity", "gift card balance tab is not active")

    def reload_amazon_gift_card(self, reload_amount):
        reload_button = self.element.get(props.amazon_giftcard_reload_button)
        reload_button.click()
        self.element.get(props.amazon_giftcard_reload_title)
        reload_field = self.element.get(props.amazon_giftcard_reload_other)
        reload_field.set_element_text(reload_amount)
        assert(reload_field.get_element_text() == reload_amount, f"Reload amount is incorrect. actual: {reload_field.get_element_text()} expected: {reload_amount}")
        print(f"clicking of buy now button")
        buy_button = self.element.get(props.amazon_giftcard_reload_buy_button)
        print("button created so now clicking")
        buy_button.click(wait_time=15)
        self.element.get(props.amazon_checkout_title)
        
    def checkout(self, card_name, card_number):
        selected_card = self.element.get(props.amazon_checkout_selected_card)
        selected_card_number = self.element.get(props.amazon_checkout_selected_card_number)
        if card_name  not in selected_card.get_element_text():
            if card_number not in selected_card_number.get_element_text():    
                change_payment = self.element.get(props.amazon_checkout_change_payment)
                change_payment.click()
                payment_cards = self.element.get(props.amazon_checkout_payment_cards, True)
                print(f"payments: {payment_cards.get_element_instance()}")
                print(f"total payment cards: {len(payment_cards.get_element_instance())}")
                for index, card in enumerate(payment_cards.get_element_instance()):
                    if card_number[-4] in card.text:
                        print(f"card found: {card.text}")
                        radio_button = self.element\
                            .get(props.amazon_checkout_new_payment_checkbox, True)\
                            .get_element_instance()[index]
                        print(f"card checkbox: {radio_button.get_property('attributes')}")
                        print(f"card checkbox: {radio_button.text}")
                        radio_button.click()
                        assert(radio_button.is_selected(), "card checkbox not selected")

        self.element.get(props.amazon_checkout_use_payment).click()
        if self.element.is_element_present(props.amazon_checkout_verify_card_input):
            card_verify = self.element.get(props.amazon_checkout_verify_card_input)
            card_verify_button = self.element.get(props.amazon_checkout_verify_card_button)
            card_verify.set_element_text(card_number)
            card_verify_button.click()

        

        
        if card_name in selected_card.get_element_text():
            if card_number in selected_card_number.get_element_text():
                raise ValueError("Card number is incorrect")

    def test_checkout(self):
        radio_button = self.element\
                            .get(props.amazon_checkout_new_payment_checkbox, True)\
                            .get_element_instance()[13]
        # print(f"card checkbox: {radio_button.get_property('attributes')}")
        print(f"card checkbox: {radio_button.text}")
        radio_button.click()

if __name__ == '__main__':
    options = None
    # options = [("debuggerAddress", "127.0.0.1:9222")]
    bm = BrowserManager()
    browser_id, browser = bm.open_browser('chrome', new_options=options)
    browser.maximize_window()
    amzn = AmazonLoginPage(browser)
    browser.get('http://www.amazon.com/')
    amzn.goto_amazon_signin_page()
    amzn.login_to_amazon("john.exantus@gmail.com", "AshteTout1206#")
    amzn.goto_amazon_gift_card_page()
    amzn.reload_amazon_gift_card(1)
    amzn.checkout("ending in 2741", "2741")
    # amzn.test_checkout()

