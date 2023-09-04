import time
from appium import webdriver
from os import path
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from appium import webdriver
from Loginscreenview import Loginscreenview
from ValidLogin import ValidLogin
from Logout import Logout
import pytest as pytest



#CURR_DIR=path.dirname(path.abspath(__file__))
#APP=path.join(CURR_DIR,"TheApp.apk")
APPIUM='http://localhost:4723'
CAPS = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'automationName': 'UiAutomator2',
    'appPackage': 'com.appiumpro.the_app',
    'appActivity': 'com.appiumpro.the_app.MainActivity',
}

# start session

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

@pytest.fixture
def homedriver(driver):
    return Loginscreenview.instance(driver)











