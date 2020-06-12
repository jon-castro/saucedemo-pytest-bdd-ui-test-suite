import os
from dotenv import load_dotenv

load_dotenv(".env", verbose=True)
CHROMEDRIVER_LOCATION = os.environ.get("CHROMEDRIVER_LOCATION", None)
SAUCEDEMO_URL = os.environ.get("SAUCEDEMO_URL", None)
LOGIN_STANDARD_USER = os.environ.get("LOGIN_STANDARD_USER", None)
LOGIN_PASSWORD = os.environ.get("LOGIN_PASSWORD", None)

# Selenium Webdriver browser selection (https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python)
