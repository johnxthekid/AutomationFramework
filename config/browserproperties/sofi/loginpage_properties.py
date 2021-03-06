from selenium.webdriver.common.by import By


# Fields on page
sofi_icon = (By.CSS_SELECTOR, "#global-top-nav a")
sofi_logo = (By.CSS_SELECTOR, "[data-qa='nav-sofi-logo']")
sofi_icon_value = "SoFi Homepage"
login_link = (By.CSS_SELECTOR, "a[data-qa='nav-log-in']")
login_page_title_value = "Log in to your account."
login_page_title = (By.CSS_SELECTOR, 'h1[data-qa="page-title"]')
login_page_email = (By.CSS_SELECTOR, 'input[data-qa="email"]')
login_page_password = (By.CSS_SELECTOR, 'input[data-qa="password"]')
login_page_submit = (By.CSS_SELECTOR, 'button[data-qa="login"]')
login_page_error = (By.CSS_SELECTOR, 'input[data-qa="password"] + span')
home_page_title = (By.CSS_SELECTOR, 'h2')

# verify page
verify_input = (By.CSS_SELECTOR, 'input')
verify_button = (By.CSS_SELECTOR, 'button[data-qa="verify"]')
remember_checkbox = (By.CSS_SELECTOR, '[data-qa="rememberMe"]')

# Homepage
nav_menu = (By.CSS_SELECTOR, '[data-qa="nav-bar-user-button"] span')  # Open Navigation
user_menu_profile = (By.CSS_SELECTOR, 'a[href$="profile"]')
user_menu_document = (By.CSS_SELECTOR, 'a[href$="document-center"]')
user_menu_membership = (By.CSS_SELECTOR, 'a[href$="membership"]')
user_menu_logout = (By.CSS_SELECTOR, 'a[href$="logout"]')