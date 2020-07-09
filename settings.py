import os
from dotenv import load_dotenv

load_dotenv(".env", verbose=True)
CHROMEDRIVER_LOCATION = os.environ.get("CHROMEDRIVER_LOCATION", None)
GECKODRIVER_LOCATION = os.environ.get("GECKODRIVER_LOCATION", None)
SAUCEDEMO_URL = os.environ.get("SAUCEDEMO_URL", None)
LOGIN_STANDARD_USER = os.environ.get("LOGIN_STANDARD_USER", None)
LOGIN_LOCKED_OUT_USER = os.environ.get("LOGIN_LOCKED_OUT_USER", None)
LOGIN_PROBLEM_USER = os.environ.get("LOGIN_PROBLEM_USER", None)
LOGIN_PERFORMANCE_GLITCH_USER = os.environ.get(
    "LOGIN_PERFORMANCE_GLITCH_USER", None)
LOGIN_PASSWORD = os.environ.get("LOGIN_PASSWORD", None)
# SCREENSHOTS_FOLDER = os.environ.get("SCREENSHOTS_FOLDER", None)
# Options: 'Chrome', 'Firefox'
SELECTED_BROWSER = 'Chrome'
# Number of unique items to add to cart from products list, 1 to 6.
ITEMS_TO_ADD_TO_CART_DURING_TESTS = 1
