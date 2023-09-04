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
time.sleep(10)
try:
    wait=WebDriverWait(driver,10)
    wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,'Login Screen')))
    wait.until(EC.presence_of_element_located((MobileBy.CLASS_NAME,'android.widget.TextView')))
    wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.TextView[@text="Webview Demo"]')))
finally:
    driver.quit()