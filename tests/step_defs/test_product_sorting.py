from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.keys import Keys
from time import sleep
from decimal import Decimal

import settings
from pages.login import LoginPage
from pages.home import HomePage
from pages.components.header import HeaderComponent

scenarios('../features/product_sorting.feature')

# When steps


@when('I sort products by price, high to low.')
def sort_products_by_price_high_to_low(browser):
    sleep(1)
    home = HomePage(browser)
    home.sort_products_by_price_high_to_low


# Then steps
@then('the first price is higher than the second price.')
def verify_if_first_price_is_higher_than_second_price(browser):
    sleep(1)
    home = HomePage(browser)
    first_price = Decimal(home.product_price_by_index_element(1).text[1:])
    second_price = Decimal(home.product_price_by_index_element(2).text[1:])
    assert first_price >= second_price

    # TODO: then - first price is lower than second price
    # TODO: then - sorted products are in alphabetical order
    # TODO: then - sorted products are in reverse alphabetical order
