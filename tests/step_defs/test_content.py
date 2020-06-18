from pytest_bdd import scenarios, given, then
from selenium.webdriver.common.keys import Keys
from time import sleep

import settings
from pages.login import LoginPage

scenarios('../features/content.feature')


# Then steps

@then('all login page content is present.')
def login_page_content_verification(browser, saucedemo_login_screen):
    login = LoginPage(browser)
    sleep(3)
    assert login.logo_element.is_displayed()
    assert login.username_field_element.is_displayed()
    assert login.password_field_element.is_displayed()
    assert login.login_button_element.is_displayed()
    assert login.accepted_usernames_list_element.is_displayed()
    assert login.accepted_usernames_list_title_element.text == login.accepted_usernames_list_title_text
    assert login.password_list_element.is_displayed()
    assert login.password_list_title_element.text == login.password_list_title_text


@then('all home page content is present.')
def home_page_content_verification(browser, standard_user_log_in):
    sleep(8)
    login = LoginPage(browser)
    assert browser.url != login.url
