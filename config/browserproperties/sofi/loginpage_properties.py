from selenium.webdriver.common.by import By


# Fields on page
sofi_icon = (By.CSS_SELECTOR, "#global-top-nav a")
sofi_logo = (By.CSS_SELECTOR, "[data-qa='nav-sofi-logo']")
sofi_icon_value = "SoFi Homepage" #'#global-top-nav a'.attributes[4].value
# login_link = (By.LINK_TEXT, "Log In")
login_link = (By.CSS_SELECTOR, "a[data-qa='nav-log-in']")
login_page_title_value = "Log in to your account."
login_page_title = (By.CSS_SELECTOR, 'h1[data-qa="page-title"]')
login_page_email = (By.CSS_SELECTOR, 'input[data-qa="email"]')
login_page_password = (By.CSS_SELECTOR, 'input[data-qa="password"]')
login_page_submit = (By.CSS_SELECTOR, 'button[data-qa="login"]')
login_page_error = (By.CSS_SELECTOR, 'input[data-qa="password"] + span')
home_page_title = (By.CSS_SELECTOR, 'h2')