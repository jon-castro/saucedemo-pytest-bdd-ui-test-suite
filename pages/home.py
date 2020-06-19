from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import settings


class HomePage:

    # Page Text

    SECONDARY_HEADER_LABEL_TEXT = "Products"
    FOOTER_COPYRIGHT_NOTICE_TEXT = "© 2019 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"

    # Page Locators

    URL = settings.SAUCEDEMO_URL + "/#/"
    SECONDARY_HEADER = "//div[@class='header_secondary_container']"
    SECONDARY_HEADER_LOGO = "//div[@class='peek']"
    SECONDARY_HEADER_LABEL = "//div[@class='product_label']"
    SECONDARY_HEADER_SORT_DROPDOWN = "//select[@class='product_sort_container']"
    SECONDARY_HEADER_SORT_DROPDOWN_AZ_OPTION = "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/select[1]/option[1]"
    SECONDARY_HEADER_SORT_DROPDOWN_AZ_OPTION = "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/select[1]/option[2]"
    SECONDARY_HEADER_SORT_DROPDOWN_LO_HI_OPTION = "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/select[1]/option[3]"
    SECONDARY_HEADER_SORT_DROPDOWN_HI_LO_OPTION = "/html[1]/body[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/select[1]/option[4]"

    def PRODUCT_SECTION_BY_INDEX(itemIndex=1):
        return "//body[@class='main-body']/div[@id='page_wrapper']/div[@id='contents_wrapper']/div[@id='inventory_container']/div/div[@id='inventory_container']/div[@class='inventory_list']/div[" + itemIndex + "]"
