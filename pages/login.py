from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import settings


class LoginPage:

    # Parameters

    standard_user = settings.LOGIN_STANDARD_USER
    password = settings.LOGIN_PASSWORD

    # Page Locators

    LOGIN_URL = settings.SAUCEDEMO_URL
    LOGO = By.XPATH, "//div[@class='login_logo']"


    def __init__(self, browser):
        self.browser = browser

    # Page Objects

    @property
    def url(self):
        return self.LOGIN_URL

    # Page Actions

    @property
    def load_login_page(self):
        self.browser.get(self.url)
