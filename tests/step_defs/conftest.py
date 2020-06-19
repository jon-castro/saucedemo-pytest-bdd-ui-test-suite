import pytest
from pytest_bdd import given, when, then
from selenium import webdriver
from pathlib import Path
from datetime import datetime

import settings
from pages.login import LoginPage


# Hooks


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')


# Hook for adding extras to the HTML report:

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # always add url to report
        extra.append(pytest_html.extras.url(settings.SAUCEDEMO_URL))

        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra


# Fixtures

@pytest.fixture
def browser():
    b = select_browser(settings.SELECTED_BROWSER)
    b.implicitly_wait(10)
    yield b
    b.quit()


# Utility functions


def select_browser(selected_browser):
    if selected_browser == 'Chrome':
        return webdriver.Chrome(executable_path=settings.CHROMEDRIVER_LOCATION)
    elif selected_browser == 'Firefox':
        return webdriver.Firefox(executable_path=settings.GECKODRIVER_LOCATION)


# def create_screenshots_folders():
#     Path(settings.SCREENSHOTS_FOLDER +
#          "/failed").mkdir(parents=True, exist_ok=True)
#     Path(settings.SCREENSHOTS_FOLDER +
#          "/test_results").mkdir(parents=True, exist_ok=True)


# def take_screenshot_on_fail(browser):
#     create_screenshots_folders()
#     timestamp = datetime.now().strftime('%H-%M-%S')
#     browser.save_screenshot(
#         settings.SCREENSHOTS_FOLDER + "/failed" + timestamp + '.png')


# Common Given steps


@given('I am on the login page.')
def saucedemo_login_screen(browser):
    login = LoginPage(browser)
    login.load_login_page


@given('I log in with the standard user.')
def standard_user_log_in(browser):
    login = LoginPage(browser)
    login.log_in_standard_user
