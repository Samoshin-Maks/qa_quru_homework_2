import pytest
from selene.support.shared import browser

@pytest.fixture
def browser_size():
    browser.config.window_width = 750
    browser.config.window_height = 1500
    browser.config.base_url = 'https://google.com'
@pytest.fixture
def open_browser(browser_size):
    browser.open(browser.config.base_url)
    print('Открытие браузера')
    yield
    browser.close()
    print('Закрытие браузера')