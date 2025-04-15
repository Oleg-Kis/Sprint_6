import pytest
from selenium import webdriver

from data import *

@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.get(main_site)
    yield browser
    browser.quit()
