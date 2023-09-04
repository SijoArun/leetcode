import time

from appium import webdriver
from os import path
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC

CURR_DIR=path.dirname(path.abspath(__file__))
APP=path.join(CURR_DIR,"TheApp.apk")
APPIUM='http://localhost:4723'

CAPS = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'automationName': 'UiAutomator2',
    'app': APP,
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)
App=path.join(CURR_DIR,"TheApp.apk")
App_Id='com.appiumpro.the_app'
try:
    driver.remove_app(App_Id)
    driver.install_app(App)
    driver.activate_app(App_Id)
    driver.terminate_app(App_Id)

finally:
    driver.quit()