from selenium.webdriver.common.by import By

# Main Page
amazon_url = "www.amazon.com"
amazon_title = "Amazon.com. Spend less. Smile more."
amazon_logo = (By.CSS_SELECTOR, '#nav-logo-sprites')
amazon_signin_tooltip = (By.CSS_SELECTOR, 'div#nav-signin-tooltip')
amazon_signin_tooltip_text = (By.CSS_SELECTOR, 'Div#nav-signin-tooltip span')
amazon_nav_account_menu = (By.CSS_SELECTOR, 'a[data-nav-role="signin"]') 
amazon_signin_text_field = (By.CSS_SELECTOR, 'a[data-nav-role="signin"] > div')

#Signin Page
amazon_signin_title = (By.CSS_SELECTOR, 'h1')  #Sign-In
amazon_signin_email = (By.CSS_SELECTOR, 'input[name="email"]')
amazon_signin_continue = (By.CSS_SELECTOR, 'input#continue')
amazon_signin_password = (By.CSS_SELECTOR, 'input[name="password"]')
amazon_signin_button = (By.CSS_SELECTOR, '#signInSubmit')
amazon_signin_button_text = (By.CSS_SELECTOR, '#signInSubmit') # Sign-In button
amazon_signout_link = (By.CSS_SELECTOR, 'a#nav-item-signout')

#Account Page
amazon_account_title = (By.CSS_SELECTOR, 'h1') # Your Account
amazon_account_giftcard = (By.CSS_SELECTOR, 'div[data-card-identifier="GiftCards"]')   # Gift cards

# Gift Card Page
amazon_giftcard_title = (By.CSS_SELECTOR, 'h2')    # Your Gift Card Balance:
amazon_giftcard_balance = (By.CSS_SELECTOR, 'h2 > span')
amazon_giftcard_balance_active_tab = (By.CSS_SELECTOR, '.gc-vertical-tab-active')  # get the value
amazon_giftcard_balance_tab = (By.CSS_SELECTOR, '#gc-vertical-tab-list > li') # first index for the balance tab. text value = View Gift Card Balance and Activity 
amazon_giftcard_reload_button = (By.CSS_SELECTOR, 'span > a.a-button-text')   # "Reload Your Balance"

# Gift Card Reload Page
amazon_giftcard_reload_title = (By.CSS_SELECTOR, '#productTitle')  # Amazon Reload
amazon_giftcard_reload_other = (By.CSS_SELECTOR, 'input[name="oneTimeReloadAmount"]')
amazon_giftcard_reload_buy_button = (By.CSS_SELECTOR, 'div[data-feature-name="buyNow"]')
amazon_giftcard_reload_button_text = (By.CSS_SELECTOR, 'input[name="submit.gc-buy-now"] + span')   # Buy Now

# Checkout Page
amazon_checkout_title = (By.CSS_SELECTOR, 'div > h1')   # Checkout
amazon_checkout_selected_card = (By.CSS_SELECTOR, 'span[data-field="cc name"]')
amazon_checkout_selected_card_number = (By.CSS_SELECTOR, '[data-field="tail"]')
amazon_checkout_change_payment = (By.ID, 'payChangeButtonId')
amazon_checkout_payment_cards = (By.CSS_SELECTOR, '[data-co-brand]')
amazon_checkout_new_payment_checkbox = (By.CSS_SELECTOR, 'label')
amazon_checkout_new_payment_card = (By.CLASS_NAME, 'pmts-cc-detail')
amazon_checkout_new_payment_number = (By.CLASS_NAME, 'span.pmts-cc-number')
amazon_checkout_payment = (By.CSS_SELECTOR, 'h3[data-testid]')     # second index for payment method
amazon_checkout_payment_card = (By.CSS_SELECTOR, 'div.pmts-instrument-box')    # look for card info
amazon_checkout_payment_card_checkbox = (By.CSS_SELECTOR, 'div.pmts-instrument-box input') # selects the card at the right index
amazon_checkout_use_payment = (By.CSS_SELECTOR, 'div.continue-buttons')
amazon_checkout_use_payment_text = (By.CSS_SELECTOR, 'input[aria-labelledby="orderSummaryPrimaryActionBtn-announce"] > span') # Use this payment method
amazon_checkout_verify_card_input = (By.CSS_SELECTOR, 'input[type="text"]')
amazon_checkout_verify_card_button = (By.CSS_SELECTOR, 'div Button')

# Order success page
amazon_success_order_text = "Order placed, thanks!"
amazon_success_order_text_tag =  (By.CSS_SELECTOR, 'h4') 
amazon_success_summary_text_tag = (By.CSS_SELECTOR, 'div[cel_widget_id="purchase-summary"] > div')
amazon_success_summary_value = (By.CSS_SELECTOR, 'div[cel_widget_id="typ-informationalMessage-0"]  span') #'div[cel_widget_id="purchase-summary"] > div>strong')
amazon_success_summary_buy_another = (By.CSS_SELECTOR, 'div > a.a-link-emphasis')

#Reload gift card page
amazon_reload_giftcard_title = (By.CSS_SELECTOR, 'h1') # Gift Cards
amazon_reload_link = (By.CSS_SELECTOR, 'li a[href*="create"]') #Reload your balance
amazon_reload_balance_link = (By.CSS_SELECTOR, 'li a[href*="balance"]') # your gift card balance