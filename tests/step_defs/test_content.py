from pytest_bdd import scenarios, given, then
from selenium.webdriver.common.keys import Keys
from time import sleep

import settings
from pages.login import LoginPage

scenarios('../features/content.feature')


# Then steps

@then('all login page content is present.')
def login_page_content_verification(browser, saucedemo_login_screen):
    # login = LoginPage(browser)
    sleep(8)
