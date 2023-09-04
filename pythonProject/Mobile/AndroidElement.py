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
try:
    wait=WebDriverWait(driver,10)
    wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,'Echo Box'))).click()
    wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'messageInput'))).send_keys("Hello")
    wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'messageSaveBtn'))).click()
    #print(driver.page_source)
    #time.sleep(100)
    saved=wait.until(EC.presence_of_element_located((MobileBy.XPATH,'//android.widget.TextView[@resource-id="savedMessage"]'))).text
    assert saved == 'Hello'
    driver.back()
    wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'Echo Box'))).click()
    saved = wait.until(
        EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.TextView[@text="Hello"]'))).text
    assert saved == 'Hello'

finally:
    driver.quit()