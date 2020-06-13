import pytest
from pytest_bdd import given, when, then
from selenium import webdriver

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
    b = webdriver.Chrome(executable_path=settings.CHROMEDRIVER_LOCATION)
    yield b
    b.quit()

# Common Given steps


@given('I am on the login page.')
def saucedemo_login_screen(browser):
    login = LoginPage(browser)
    login.load_login_page
