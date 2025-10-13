import pytest
from selene import browser


@pytest.fixture
def new_setup_for_browser():
    browser.config.window_width = '1920'
    browser.config.window_height = '1080'

