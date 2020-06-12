from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import settings


class LoginPage:

    # Page Locators

    URL = settings.SAUCEDEMO_URL

    def __init__(self, browser):
        self.browser = browser

    # Page Objects

    @property
    def url(self):
        return self.URL

    # Page Actions

    @property
    def load_login_page(self):
        self.browser.get(self.url)
