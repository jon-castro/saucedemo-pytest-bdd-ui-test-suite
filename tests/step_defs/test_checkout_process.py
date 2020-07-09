from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.keys import Keys
from time import sleep
from decimal import Decimal

import settings
from pages.login import LoginPage
from pages.home import HomePage
from pages.components.header import HeaderComponent

scenarios('../features/checkout_process.feature')

# When steps


# Then steps
