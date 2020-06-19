from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import settings


class HeaderComponent:

    # Component Locators

    HEADER = By.XPATH, "//div[@id='header_container']"
    MENU_BUTTON = By.XPATH, "//div[@class='bm-burger-button']"
    CART_BUTTON = By.XPATH, "//a[@class='shopping_cart_link fa-layers fa-fw']//*[local-name()='svg']"
    CART_BADGE = By.XPATH, "//span[@class='fa-layers-counter shopping_cart_badge']"
    SIDE_MENU = By.XPATH, "//div[@class='bm-menu']"
    SIDE_MENU_CLOSE_BUTTON = By.XPATH, "//div[@class='bm-cross-button']"
    SIDE_MENU_ALL_ITEMS_LINK = By.XPATH, "//a[@id='inventory_sidebar_link']"
    SIDE_MENU_ABOUT_LINK = By.XPATH, "//a[@id='about_sidebar_link']"
    SIDE_MENU_LOGOUT_LINK = By.XPATH, "//a[@id='logout_sidebar_link']"
    SIDE_MENU_RESET_APP_LINK = By.XPATH, "//a[@id='reset_sidebar_link']"

    def __init__(self, browser):
        self.browser = browser

    # Component Objects

    @property
    def header_element(self):
        return self.browser.find_element(*self.HEADER)

    @property
    def menu_button_element(self):
        return self.browser.find_element(*self.MENU_BUTTON)

    @property
    def cart_button_element(self):
        return self.browser.find_element(*self.CART_BUTTON)

    @property
    def cart_badge_element(self):
        return self.browser.find_element(*self.CART_BADGE)

    @property
    def side_menu_element(self):
        return self.browser.find_element(*self.SIDE_MENU)

    @property
    def side_menu_close_button_element(self):
        return self.browser.find_element(*self.SIDE_MENU_CLOSE_BUTTON)

    @property
    def side_menu_all_items_link_element(self):
        return self.browser.find_element(*self.SIDE_MENU_ALL_ITEMS_LINK)

    @property
    def side_menu_about_link_element(self):
        return self.browser.find_element(*self.SIDE_MENU_ABOUT_LINK)

    @property
    def side_menu_about_link_element(self):
        return self.browser.find_element(*self.SIDE_MENU_ABOUT_LINK)

    @property
    def side_menu_logout_link_element(self):
        return self.browser.find_element(*self.SIDE_MENU_LOGOUT_LINK)

    @property
    def side_menu_reset_app_link_element(self):
        return self.browser.find_element(*self.SIDE_MENU_RESET_APP_LINK)

    # Page Actions

    @property
    def click_menu_button(self):
        self.menu_button_element.click()

    @property
    def click_cart_button(self):
        self.cart_button_element.click()

    @property
    def click_side_menu_close_button(self):
        self.side_menu_close_button_element.click()

    @property
    def click_side_menu_all_items_link(self):
        self.side_menu_all_items_link_element.click()

    @property
    def click_side_menu_about_link(self):
        self.side_menu_about_link_element.click()

    @property
    def click_side_menu_logout_link(self):
        self.side_menu_logout_link_element.click()

    @property
    def click_side_menu_reset_app_link(self):
        self.side_menu_reset_app_link_element.click()
