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
    FOOTER_SECTION = By.XPATH, "/html[1]/body[1]/footer[1]"
    FOOTER_COPYRIGHT_NOTICE = By.XPATH, "/html[1]/body[1]/footer[1]/div[1]"

    def __init__(self, browser):
        self.browser = browser

    # Page Objects

    @property
    def url(self):
        return self.HOME_URL

    @property
    def secondary_header_element(self):
        return self.browser.find_element(*self.SECONDARY_HEADER)

    @property
    def secondary_header_logo_element(self):
        return self.browser.find_element(*self.SECONDARY_HEADER_LOGO)

    @property
    def secondary_header_label_element(self):
        return self.browser.find_element(*self.SECONDARY_HEADER_LABEL)

    @property
    def secondary_header_label_text(self):
        return self.SECONDARY_HEADER_LABEL_TEXT

    @property
    def secondary_header_sort_dropdown_element(self):
        return self.browser.find_element(*self.SECONDARY_HEADER_SORT_DROPDOWN)

    @property
    def secondary_header_sort_dropdown_az_option_element(self):
        return self.browser.find_element(*self.SECONDARY_HEADER_SORT_DROPDOWN_AZ_OPTION)

    @property
    def secondary_header_sort_dropdown_za_option_element(self):
        return self.browser.find_element(*self.SECONDARY_HEADER_SORT_DROPDOWN_ZA_OPTION)

    @property
    def secondary_header_sort_dropdown_lo_hi_option_element(self):
        return self.browser.find_element(*self.SECONDARY_HEADER_SORT_DROPDOWN_LO_HI_OPTION)

    @property
    def secondary_header_sort_dropdown_hi_lo_option_element(self):
        return self.browser.find_element(*self.SECONDARY_HEADER_SORT_DROPDOWN_HI_LO_OPTION)

    def product_section_by_index_element(self, item_index=1):
        return self.browser.find_element(By.XPATH, "//body[@class='main-body']/div[@id='page_wrapper']/div[@id='contents_wrapper']/div[@id='inventory_container']/div/div[@id='inventory_container']/div[@class='inventory_list']/div[" + str(item_index) + "]")

    def product_image_by_index_element(self, item_index=1):
        return self.browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[" + str(item_index) + "]/div[1]/a[1]")

    def product_name_by_index_element(self, item_index=1):
        return self.browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[" + str(item_index) + "]/div[2]/a[1]/div[1]")

    def product_description_by_index_element(self, item_index=1):
        return self.browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[" + str(item_index) + "]/div[2]/div[1]")

    def product_price_by_index_element(self, item_index=1):
        return self.browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[" + str(item_index) + "]/div[3]/div[1]")

    def product_add_to_cart_button_by_index_element(self, item_index=1):
        return self.browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[" + str(item_index) + "]/div[3]/button[1]")

    @property
    def footer_section_element(self):
        return self.browser.find_element(*self.FOOTER_SECTION)

    @property
    def footer_copyright_notice_element(self):
        return self.browser.find_element(*self.FOOTER_COPYRIGHT_NOTICE)

    @property
    def footer_copyright_notice_text(self):
        return self.FOOTER_COPYRIGHT_NOTICE_TEXT

    # Page Actions

    @property
    def sort_products_by_price_high_to_low(self):
        self.secondary_header_sort_dropdown_element.click()
        self.secondary_header_sort_dropdown_hi_lo_option_element.click()

    @property
    def sort_products_by_price_low_to_high(self):
        self.secondary_header_sort_dropdown_element.click()
        self.secondary_header_sort_dropdown_lo_hi_option_element.click()

    @property
    def sort_products_in_alphabetical_order(self):
        self.secondary_header_sort_dropdown_element.click()
        self.secondary_header_sort_dropdown_az_option_element.click()

    @property
    def sort_products_in_reverse_alphabetical_order(self):
        self.secondary_header_sort_dropdown_element.click()
        self.secondary_header_sort_dropdown_za_option_element.click()

    def select_product_name_by_index_element(self, item_index):
        self.product_name_by_index_element(item_index).click()

    def select_product_image_by_index_element(self, item_index):
        self.product_image_by_index_element(item_index).click()

    @property
    def add_products_to_cart(self):
        for x in settings.ITEMS_TO_ADD_TO_CART_DURING_TESTS:
            self.product_add_to_cart_button_by_index_element(x).click()
