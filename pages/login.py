from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import settings


class LoginPage:

    # Parameters

    STANDARD_USER = settings.LOGIN_STANDARD_USER
    LOCKED_OUT_USER = settings.LOGIN_LOCKED_OUT_USER
    PROBLEM_USER = settings.LOGIN_PROBLEM_USER
    PERFORMANCE_GLITCH_USER = settings.LOGIN_PERFORMANCE_GLITCH_USER
    PASSWORD = settings.LOGIN_PASSWORD

    # Page Text

    ACCEPTED_USERNAMES_LIST_TITLE_TEXT = "Accepted usernames are:"
    PASSWORD_LIST_TITLE_TEXT = "Password for all users:"
    LOCKED_OUT_USER_ERROR_MESSAGE_TEXT = "Epic sadface: Sorry, this user has been locked out."

    # Page Locators

    LOGIN_URL = settings.SAUCEDEMO_URL
    LOGO = By.XPATH, "//div[@class='login_logo']"
    USERNAME_FIELD = By.XPATH, "//input[@id='user-name']"
    PASSWORD_FIELD = By.XPATH, "//input[@id='password']"
    LOGIN_BUTTON = By.XPATH, "//input[@class='btn_action']"
    BOT_IMAGE = By.XPATH, "//div[@class='bot_column']"
    ACCEPTED_USERNAMES_LIST = By.XPATH, "//div[@id='login_credentials']"
    ACCEPTED_USERNAMES_LIST_TITLE = By.XPATH, "//h4[contains(text(),'Accepted usernames are:')]"
    PASSWORD_LIST = By.XPATH, "//div[@class='login_password']"
    PASSWORD_LIST_TITLE = By.XPATH, "//h4[contains(text(),'Password for all users:')]"
    LOGIN_ERROR_BUTTON = By.XPATH, "//button[@class='error-button']//*[local-name()='svg']"
    LOCKED_OUT_USER_ERROR_MESSAGE = By.XPATH, "//h3[1]"

    def __init__(self, browser):
        self.browser = browser

    # Page Objects

    @property
    def url(self):
        return self.LOGIN_URL

    @property
    def logo_element(self):
        return self.browser.find_element(*self.LOGO)

    @property
    def username_field_element(self):
        return self.browser.find_element(*self.USERNAME_FIELD)

    @property
    def password_field_element(self):
        return self.browser.find_element(*self.PASSWORD_FIELD)

    @property
    def login_button_element(self):
        return self.browser.find_element(*self.LOGIN_BUTTON)

    @property
    def bot_image_element(self):
        return self.browser.find_element(*self.BOT_IMAGE)

    @property
    def accepted_usernames_list_element(self):
        return self.browser.find_element(*self.ACCEPTED_USERNAMES_LIST)

    @property
    def accepted_usernames_list_title_element(self):
        return self.browser.find_element(*self.ACCEPTED_USERNAMES_LIST_TITLE)

    @property
    def accepted_usernames_list_title_text(self):
        return self.ACCEPTED_USERNAMES_LIST_TITLE_TEXT

    @property
    def password_list_element(self):
        return self.browser.find_element(*self.PASSWORD_LIST)

    @property
    def password_list_title_element(self):
        return self.browser.find_element(*self.PASSWORD_LIST_TITLE)

    @property
    def password_list_title_text(self):
        return self.PASSWORD_LIST_TITLE_TEXT

    @property
    def login_error_button_element(self):
        return self.browser.find_element(*self.LOGIN_ERROR_BUTTON)

    @property
    def locked_out_user_error_message_element(self):
        return self.browser.find_element(*self.LOCKED_OUT_USER_ERROR_MESSAGE)

    @property
    def locked_out_user_error_message_text(self):
        return self.LOCKED_OUT_USER_ERROR_MESSAGE_TEXT

    # Page Actions

    @property
    def load_login_page(self):
        self.browser.get(self.url)
        self.browser.maximize_window()

    def enter_username(self, username):
        try:
            self.username_field_element.send_keys('asas')
        except:
            self.save_screenshot('screenshots/failed/' +
                                 self.enter_username.__name__ + '.png')
            print('Step ' + self.enter_username.__name__ + ' failed.')

    @property
    def enter_password(self):
        try:
            self.password_field_element.send_keys(settings.LOGIN_PASSWORD)
        except:
            # Failed screenshot
            print('Step ' + self.enter_password.__name__ + ' failed.')

    @property
    def click_login_button(self):
        try:
            self.login_button_element.click()
        except:
            # Failed screenshot
            print('Step ' + self.click_login_button.__name__ + ' failed.')

    @property
    def log_in_standard_user(self):
        try:
            self.load_login_page
            self.enter_username(self.STANDARD_USER)
            self.enter_password
            self.click_login_button
        except:
            # Failed screenshot
            print('Step ' + self.log_in_standard_user.__name__ + ' failed.')

    @property
    def log_in_locked_out_user(self):
        try:
            self.load_login_page
            self.enter_username(self.LOCKED_OUT_USER)
            self.enter_password
            self.click_login_button
        except:
            # Failed screenshot
            print('Step ' + self.log_in_locked_out_user.__name__ + ' failed.')

    @property
    def click_locked_out_user_error_button(self):
        try:
            self.login_error_button_element.click()
        except:
            # Failed screenshot
            print('Step ' + self.click_locked_out_user_error_button.__name__ + ' failed.')

    @property
    def log_in_problem_user(self):
        try:
            self.load_login_page
            self.enter_username(self.PROBLEM_USER)
            self.enter_password
            self.click_login_button
        except:
            # Failed screenshot
            print('Step ' + self.log_in_problem_user.__name__ + ' failed.')

    @property
    def log_in_performance_glitch_user(self):
        try:
            self.load_login_page
            self.enter_username(self.PERFORMANCE_GLITCH_USER)
            self.enter_password
            self.click_login_button
        except:
            # Failed screenshot
            print('Step ' + self.log_in_performance_glitch_user.__name__ + ' failed.')
