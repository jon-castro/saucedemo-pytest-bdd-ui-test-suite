from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import settings


class HomePage:

    # Page Text

    SECONDARY_HEADER_LABEL_TEXT = "Products"
    FOOTER_COPYRIGHT_NOTICE_TEXT = "© 2019 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"

    # Page Locators

    HOME_URL = settings.SAUCEDEMO_URL + "/inventory.html"
    SECONDARY_HEADER = By.XPATH, "//div[@class='header_secondary_container']"
    SECONDARY_HEADER_LOGO = By.XPATH, "//div[@class='peek']"
    SECONDARY_HEADER_LABEL = By.XPATH, "//div[@class='product_label']"
    SECONDARY_HEADER_SORT_DROPDOWN = By.XPATH, "//select[@class='product_sort_container']"
    SECONDARY_HEADER_SORT_DROPDOWN_AZ_OPTION = By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/select[1]/option[1]"
    SECONDARY_HEADER_SORT_DROPDOWN_ZA_OPTION = By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/select[1]/option[2]"
    SECONDARY_HEADER_SORT_DROPDOWN_LO_HI_OPTION = By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/select[1]/option[3]"
    SECONDARY_HEADER_SORT_DROPDOWN_HI_LO_OPTION = By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/select[1]/option[4]"

    def PRODUCT_SECTION_BY_INDEX(item_index=1):
        xpath = "//body[@class='main-body']/div[@id='page_wrapper']/div[@id='contents_wrapper']/div[@id='inventory_container']/div/div[@id='inventory_container']/div[@class='inventory_list']/div[" + item_index + "]"
        return By.XPATH, xpath

    def PRODUCT_IMAGE_BY_INDEX(item_index=1):
        xpath = "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[" + \
            item_index + "]/div[1]/a[1]"
        return By.XPATH, xpath

    def PRODUCT_NAME_BY_INDEX(item_index=1):
        xpath = "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[" + \
            item_index + "]/div[2]/a[1]/div[1]"
        return By.XPATH, xpath

    def PRODUCT_DESCRIPTION_BY_INDEX(item_index=1):
        xpath = "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[" + \
            item_index + "]/div[2]/div[1]"
        return By.XPATH, xpath

    def PRODUCT_PRICE_BY_INDEX(item_index=1):
        xpath = "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[" + \
            item_index + "]/div[3]/div[1]"
        return By.XPATH, xpath

    def PRODUCT_ADD_TO_CART_BUTTON_BY_INDEX(item_index=1):
        xpath = "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[" + \
            item_index + "]/div[3]/button[1]"
        return By.XPATH, xpath

    FOOTER_SECTION = By.XPATH, "/html[1]/body[1]/footer[1]"
    FOOTER_COPYRIGHT_NOTICE = By.XPATH, "/html[1]/body[1]/footer[1]/div[1]"

    def __init__(self, browser):
        self.browser = browser

    # Page Objects

    @property
    def url(self):
        return self.HOME_URL

    @property
    def secondary_header(self):
        return self.browser.find_element(*self.SECONDARY_HEADER)

    @property
    def secondary_header_logo(self):
        return self.browser.find_element(*self.SECONDARY_HEADER_LOGO)

    @property
    def secondary_header_label(self):
        return self.browser.find_element(*self.SECONDARY_HEADER_LABEL)

    @property
    def secondary_header_sort_dropdown(self):
        return self.browser.find_element(*self.SECONDARY_HEADER_SORT_DROPDOWN)

    @property
    def secondary_header_sort_dropdown_az_option(self):
        return self.browser.find_element(*self.SECONDARY_HEADER_SORT_DROPDOWN_AZ_OPTION)

    @property
    def secondary_header_sort_dropdown_za_option(self):
        return self.browser.find_element(*self.SECONDARY_HEADER_SORT_DROPDOWN_ZA_OPTION)

    @property
    def secondary_header_sort_dropdown_lo_hi_option(self):
        return self.browser.find_element(*self.SECONDARY_HEADER_SORT_DROPDOWN_LO_HI_OPTION)

    @property
    def secondary_header_sort_dropdown_hi_lo_option(self):
        return self.browser.find_element(*self.SECONDARY_HEADER_SORT_DROPDOWN_HI_LO_OPTION)

    def product_section_by_index(self, item_index):
        return self.browser.find_element(self.PRODUCT_SECTION_BY_INDEX(item_index))

    def product_image_by_index(self, item_index):
        return self.browser.find_element(self.PRODUCT_IMAGE_BY_INDEX(item_index))

    def product_name_by_index(self, item_index):
        return self.browser.find_element(self.PRODUCT_NAME_BY_INDEX(item_index))

    def product_description_by_index(self, item_index):
        return self.browser.find_element(self.PRODUCT_DESCRIPTION_BY_INDEX(item_index))

    def product_price_by_index(self, item_index):
        return self.browser.find_element(self.PRODUCT_PRICE_BY_INDEX(item_index))

    def product_add_to_cart_button_by_index(self, item_index):
        return self.browser.find_element(self.PRODUCT_ADD_TO_CART_BUTTON_BY_INDEX(item_index))

    @property
    def footer_section(self):
        return self.browser.find_element(*self.FOOTER_SECTION)

    @property
    def footer_copyright_notice(self):
        return self.browser.find_element(*self.FOOTER_COPYRIGHT_NOTICE)

    # Page Actions
