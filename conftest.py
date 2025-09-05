import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="function")
def setup_browser():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    browser.config.driver = driver


@pytest.fixture(scope="function")
def setup_resolution(setup_browser):
    browser.config.window_width = 1920
    browser.config.window_height = 1080
