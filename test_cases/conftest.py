import pytest
from selenium import webdriver
from pytest_metadata.plugin import metadata_key

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Specify browser Chrome, Firefox or Edge")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("unsupported browser")
    return driver

############HTML report customization######################3

def pytest_configure(config):
    config.stash[metadata_key] ["Project Name"] = 'OrangeHRM'
    config.stash[metadata_key] ["Test Module Name"] = 'Login tests'
    config.stash[metadata_key]["Tester"] = 'Sujay'

# Hooks to remove the unwanted details from test report
def pytest_metadata(metadata):
    metadata.pop("Plugins", None)




