import time
import pytest as pytest
from appium import webdriver
from os import path
from viewpage.homeview import homeviewscreen


CURR_DIR=path.dirname(path.abspath(__file__))
APP=path.join(CURR_DIR,"..","Mobile","TheApp.app.zip")
APPIUM='http://localhost:4723'

@pytest.fixture
def driver():
    CAPS = {
    'platformName': 'iOS',
    'platformVersion': '16.4',
    'deviceName': 'iPhone 14 Pro Max',
    'automationName': 'XCUITest',
    'app': APP,
    }
    driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
    )
    yield driver
    driver.quit()

@pytest.fixture
def home(driver):
    return homeviewscreen(driver)