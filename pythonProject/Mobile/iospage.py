import time
from appium import webdriver
from os import path
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC

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
try:
    wait=WebDriverWait(driver,10)
    wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,'Login Screen')))
    print(driver.page_source)
finally:
    driver.quit()