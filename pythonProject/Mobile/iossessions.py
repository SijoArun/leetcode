import time

from appium import webdriver
from os import path

CURR_DIR=path.dirname(path.abspath(__file__))
APP=path.join(CURR_DIR,"TheApp.app.zip")
APPIUM='http://localhost:4723'

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
time.sleep(10)
driver.quit()