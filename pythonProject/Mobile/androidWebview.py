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
class webview_context(object):
    def __call__(self,driver):
        for context in driver.contexts:
            if context!= 'NATIVE_APP':
                driver.switch_to.context(context)
                return True
        return False


try:
    wait=WebDriverWait(driver,10)
    wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID,'Webview Demo'))).click()
    wait.until(EC.presence_of_element_located((MobileBy.XPATH,
                                               '//XCUIElementTypeTextField[@name="urlInput"]'))).send_keys("https://appiumpro.com")
    wait.until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, 'navigateBtn'))).click()
    wait.until(webview_context())
    print(driver.current_url)
    print(driver.title)

finally:
    driver.quit()


