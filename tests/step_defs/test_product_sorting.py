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


@when('I sort products by price, low to high.')
def sort_products_by_price_high_to_low(browser):
    sleep(1)
    home = HomePage(browser)
    home.sort_products_by_price_low_to_high


@when('I sort products in alphabetical order.')
def sort_products_in_alphabetical_order(browser):
    sleep(1)
    home = HomePage(browser)
    home.sort_products_in_alphabetical_order


@when('I sort products in reverse alphabetical order.')
def sort_products_in_reverse_alphabetical_order(browser):
    sleep(1)
    home = HomePage(browser)
    home.sort_products_in_reverse_alphabetical_order


# Then steps


@then('the first price is higher than the second price.')
def verify_if_first_price_is_higher_than_second_price(browser):
    sleep(1)
    home = HomePage(browser)
    first_price = Decimal(home.product_price_by_index_element(1).text[1:])
    second_price = Decimal(home.product_price_by_index_element(2).text[1:])
    assert first_price >= second_price


@then('the first price is lower than the second price.')
def verify_if_first_price_is_lower_than_second_price(browser):
    sleep(1)
    home = HomePage(browser)
    first_price = Decimal(home.product_price_by_index_element(1).text[1:])
    second_price = Decimal(home.product_price_by_index_element(2).text[1:])
    assert first_price <= second_price


@then('the sorted products are in alphabetical order.')
def verify_if_sorted_products_are_in_alphabetical_order(browser):
    sleep(1)
    home = HomePage(browser)
    products_list = []
    first_product = home.product_name_by_index_element(1).text
    second_product = home.product_name_by_index_element(2).text
    products_list.append(first_product)
    products_list.append(second_product)
    products_list.sort()
    assert first_product == products_list[0]
    assert second_product == products_list[1]


@then('the sorted products are in reverse alphabetical order.')
def verify_if_sorted_products_are_in_reverse_alphabetical_order(browser):
    sleep(1)
    home = HomePage(browser)
    products_list = []
    first_product = home.product_name_by_index_element(1).text
    second_product = home.product_name_by_index_element(2).text
    products_list.append(first_product)
    products_list.append(second_product)
    products_list.sort()
    products_list.reverse()
    assert first_product == products_list[0]
    assert second_product == products_list[1]
