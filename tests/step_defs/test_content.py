from pytest_bdd import scenarios, given, then
from selenium.webdriver.common.keys import Keys
from time import sleep

import settings
from pages.login import LoginPage
from pages.home import HomePage
from pages.components.header import HeaderComponent

scenarios('../features/content.feature')


# Then steps

@then('all login page content is present.')
def login_page_content_verification(browser, saucedemo_login_screen):
    login = LoginPage(browser)
    sleep(1)
    assert login.logo_element.is_displayed(), "Logo not present."
    assert login.username_field_element.is_displayed(), "Username field not present."
    assert login.password_field_element.is_displayed(), "Password field not present."
    assert login.login_button_element.is_displayed(), "Login button not present."
    assert login.accepted_usernames_list_element.is_displayed(
    ), "Accepted Usernames List not present."
    assert login.accepted_usernames_list_title_element.text == login.accepted_usernames_list_title_text
    assert login.password_list_element.is_displayed(), "Password List not present."
    assert login.password_list_title_element.text == login.password_list_title_text


@then('all header component content is present.')
def header_component_content_verification(browser, standard_user_log_in):
    header = HeaderComponent(browser)
    assert header.header_element.is_displayed(), "Header not present."
    assert header.menu_button_element.is_displayed(), "Menu button not present."
    assert header.cart_button_element.is_displayed(), "Cart button not present."
    header.click_menu_button
    sleep(1)
    assert header.side_menu_close_button_element.is_displayed(), "Close button not present."
    assert header.side_menu_all_items_link_element.is_displayed(
    ), "All Items link not present."
    assert header.side_menu_about_link_element.is_displayed(), "About link not present."
    assert header.side_menu_logout_link_element.is_displayed(), "Logout link not present."
    assert header.side_menu_reset_app_link_element.is_displayed(
    ), "Reset App link not present."


@then('all home page content is present.')
def home_page_content_verification(browser):
    sleep(1)
    home = HomePage(browser)
    assert browser.current_url == home.url
    assert home.secondary_header_element.is_displayed(), "Header not present."
    assert home.secondary_header_logo_element.is_displayed(), "Header logo not present."
    assert home.secondary_header_label_element.text == home.secondary_header_label_text
    assert home.secondary_header_sort_dropdown_element.is_displayed(), "Product sort dropdown not present."
    assert home.secondary_header_sort_dropdown_az_option_element.is_displayed(), "Product sort dropdown option not present."
    assert home.secondary_header_sort_dropdown_za_option_element.is_displayed(), "Product sort dropdown option not present."
    assert home.secondary_header_sort_dropdown_hi_lo_option_element.is_displayed(), "Product sort dropdown option not present."
    assert home.secondary_header_sort_dropdown_lo_hi_option_element.is_displayed(), "Product sort dropdown option not present."
    assert home.product_section_by_index_element(1).is_displayed(), "Product section not present."
    assert home.product_image_by_index_element(1).is_displayed(), "Product image not present."
    assert home.product_name_by_index_element(1).is_displayed(), "Product name not present."
    assert home.product_description_by_index_element(1).is_displayed(), "Product description not present."
    assert home.product_price_by_index_element(1).is_displayed(), "Product price not present."
    assert home.product_add_to_cart_button_by_index_element(1).is_displayed(), "Product add to cart button not present."
    assert home.footer_section_element.is_displayed(), "Footer section not present."
    assert home.footer_copyright_notice_element.text == home.footer_copyright_notice_text

    # TODO: then - first price is higher than second price
    # TODO: then - first price is lower than second price
    # TODO: then - sorted products are in alphabetical order
    # TODO: then - sorted products are in reverse alphabetical order
