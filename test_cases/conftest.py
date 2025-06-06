import pytest
from selenium import webdriver


def pytest_addoption(parser):  # This get the value from CLI /hooks
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests (chrome/firefox/edge)")


@pytest.fixture()
def browser(request):  # * This return the Browser value to setup method
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    driver = None

    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome")

    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox")

    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge")

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    return driver


############# PYTEST HTML REPORT #################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    # Only set metadata if pytest-html plugin is active
    if hasattr(config, '_metadata'):
        config._metadata['Project Name'] = 'orange_hrm'
        config._metadata['Module Name'] = 'Customers'
        config._metadata['Tester'] = 'Varunreddy'


# Optional hook for customizing environment info in pytest-html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
