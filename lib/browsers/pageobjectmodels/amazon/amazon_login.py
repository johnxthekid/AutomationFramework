import sys
from os import path, environ

from selenium.common.exceptions import ErrorInResponseException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
sys.path.append(path.join(path.dirname(__file__), "..", "..", "..", ".."))

from robot.api import logger

from lib.browsers.drivermanagers.BrowserManager import BrowserManager
from lib.browsers.drivermanagers.BrowserElementActions import ElementActions
import config.browserproperties.amazon.loginpage_properties as props


class AmazonLoginPage:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    _browser = None
    element = None

    def __init__(self, browser):
        self._browser = browser
        self.element = ElementActions(self._browser)

    def __exit__(self, exception_type, exception_value, traceback):
        self._browser.quit()

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
        username.set_element_text(username_value)
        print(f"user name typed: {username.get_element_text()}")
        assert(username.get_element_text() != "", f"{username.get_element_text()}")
        continue_button.click()
        assert(self.element.is_element_present(props.amazon_signin_password), "password page not displayed")
        password = self.element.get(props.amazon_signin_password)
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
        assert(self.element.is_element_present(props.amazon_giftcard_balance), "Giftcard reload page not displayed")
        gitfcard_balance = self.element.get(props.amazon_giftcard_balance)
        print(f"current balance: {gitfcard_balance.get_element_text()}")
        giftcard_balance_tab = self.element.get(props.amazon_giftcard_balance_tab)
        giftcard_balance_tab.click()
        assert(giftcard_balance_tab.get_element_text() == "View Gift Card Balance and Activity", "gift card balance tab is not active")

    def goto_giftcard_reload_page(self):
        reload_button = self.element.get(props.amazon_giftcard_reload_button)
        reload_button.click()
        self.element.get(props.amazon_giftcard_reload_title)
    
    def reload_amazon_gift_card(self, reload_amount):
        reload_field = self.element.get(props.amazon_giftcard_reload_other)
        reload_field.set_element_text(reload_amount)
        assert(reload_field.get_element_text() == reload_amount, f"Reload amount is incorrect. actual: {reload_field.get_element_text()} expected: {reload_amount}")
        print(f"clicking of buy now button")
        buy_button = self.element.get(props.amazon_giftcard_reload_buy_button)
        print("button created so now clicking")
        buy_button.click(wait_time=15)
        self.element.get(props.amazon_checkout_title)
        
    def checkout(self, card_name, card_number):
        buy_button = self.element.get(props.amazon_checkout_use_payment)
        if not "Use this payment" in buy_button.get_element_text():
            selected_card = self.element.get(props.amazon_checkout_selected_card)
            selected_card_number = self.element.get(props.amazon_checkout_selected_card_number)
  
            change_payment = self.element.get(props.amazon_checkout_change_payment)
            change_payment.click()
        payment_cards = self.element.get(props.amazon_checkout_payment_cards, True)
        print(f"payments: {payment_cards.get_element_instance()}")
        print(f"total payment cards: {len(payment_cards.get_element_instance())}")
        for card in payment_cards.get_element_instance():
            if card_number[-4:] in card.text:
                print(f"card found: {card.text}")
                radio_button = self.element\
                    .get_sub_element(props.amazon_checkout_new_payment_checkbox, parent=card)
                print(f"card checkbox: {radio_button.get_element_text()}")
                radio_button.click(validate=False)
                assert(radio_button.is_selected(), "card checkbox not selected")

                buy_button.click()
                if not self.element.is_element_present(props.amazon_checkout_change_payment, wait_time=5):
                    card_verify = self.element\
                        .get_sub_element(props.amazon_checkout_verify_card_input, parent=card)
                    card_verify_button = self.element\
                        .get_sub_element(props.amazon_checkout_verify_card_button, parent=card)
                    if card_verify_button.wait_visible(wait_time=5):
                        print(f"properties: \n{card_verify.get_element_properties()}")
                        card_verify.set_element_text(card_number)
                        assert(card_number == card_verify.get_element_text(), f"card number entered is incorrect. value: {card_verify.get_element_text()}")
                        card_verify_button.click(validate=False) 
                        card_verify_button.wait_visible(False, wait_time=4) 
                        buy_button.click()
                break  
        
        selected_card = self.element.get(props.amazon_checkout_selected_card)
        selected_card_number = self.element.get(props.amazon_checkout_selected_card_number)
        assert(card_name in selected_card.get_element_text(), f"Incorrect card selected, {selected_card.get_element_text()}")
        if card_name in selected_card.get_element_text():
            if card_number in selected_card_number.get_element_text():
                raise ValueError("Card number is incorrect")

        # finalize payment
        buy_button.reload_element()
        assert("place your order" in buy_button.get_element_text(), f"Incorrect label on buy button. Text: {buy_button.get_element_text()}")
        buy_button.click()
        assert(self.element.is_element_present(props.amazon_success_order_text_tag), "Success order page title not found")
        success_title = self.element.get(props.amazon_success_order_text_tag)
        assert(props.amazon_success_order_text in success_title.get_element_text(), f"success text not displayed. text: {success_title.get_element_text()}")
        order_ammount = self.element.get(props.amazon_success_summary_value)
        print(f"order amount: {order_ammount.get_element_text()}")

    def buy_more_giftcard(self):
        buy_another = self.element.get(props.amazon_success_summary_buy_another)
        print(f"buy another text: {buy_another.get_element_text()}")
        assert(("Send another Gift Card" == buy_another.get_element_text()), f"link text incorrect, text: {buy_another.get_element_text()}")
        buy_another.click()
        assert(self.element.is_element_present(props.amazon_reload_giftcard_title), "Reload giftcard page not displayed.")
        assert("Gift Cards" in self.element.get(props.amazon_reload_giftcard_title).get_element_text(), f"reload page title incorrect. text: {props.amazon_reload_giftcard_title}")
        reload_link = self.element.get(props.amazon_reload_link)
        reload_link.click()
        assert(self.element.is_element_present(props.amazon_giftcard_reload_title), "giftcard reload page not displayed")
        

if __name__ == '__main__':
    options = None
    user = environ.get('amzn_user')
    pwd = environ.get('amzn_password')
    card = environ.get('amzn_tmobile')
    # options = [("debuggerAddress", "127.0.0.1:9222")]
    bm = BrowserManager()
    browser_id, browser = bm.open_browser('chrome', new_options=options)
    browser.maximize_window()
    amzn = AmazonLoginPage(browser)
    browser.get('http://www.amazon.com/')
    amzn.goto_amazon_signin_page()
    amzn.login_to_amazon(user, pwd)
    amzn.goto_amazon_gift_card_page()
    amzn.goto_giftcard_reload_page()
    for _ in range(2):
        amzn.reload_amazon_gift_card(1) 
        amzn.checkout(f"ending in {card[-4:]}", card)
        amzn.buy_more_giftcard()
