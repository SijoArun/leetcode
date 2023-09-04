import time
from appium import webdriver
from os import path
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.mouse_button import MouseButton
from appium.webdriver.common.touch_action import TouchAction



CURR_DIR=path.dirname(path.abspath(__file__))
APP=path.join(CURR_DIR,"TheApp.apk")
#APPIUM='http://localhost:4723'
APPIUM='https://dev-us-pao-0.headspin.io:7045/v0/1f7e749a3421489fa8e618610b3e2740/wd/hub'

'''
CAPS = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'automationName': 'UiAutomator2',
    'app': '/Users/sijo/PycharmProjects/pythonProject/Mobile/TheApp.apk',
    'headspin:capture.video': True,
    'headspin:autoDownloadChromedriver': True,
}
'''
CAPS = {
    'platformName': 'Android',
    'deviceName': 'SM-A715F',
    'automationName': 'uiautomator2',
    'headspin:autoDownloadChromedriver': True,
    "udid": 'R58N92C0XEZ',
    #'app': "/Users/sijo/PycharmProjects/pythonProject/Mobile/TheApp.apk",
    'appPackage': 'com.appiumpro.the_app',
    'appActivity': 'com.appiumpro.the_app.MainActivity',
    'headspin:capture.video': True,
}

webview=(MobileBy.XPATH,'//android.widget.TextView[@text="Webview Demo"]')
urlInput=(MobileBy.XPATH, '//android.widget.EditText[@content-desc="urlInput"]')
go=(MobileBy.XPATH, '//android.widget.TextView[@text="Go"]')
ok=(MobileBy.XPATH, '//android.widget.TextView[@text="OK"]')
clear=(MobileBy.XPATH, '//android.widget.TextView[@text="Clear"]')
element=(By.LINK_TEXT, "Form Authentication")


driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)


try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(webview)).click()
    wait.until(EC.presence_of_element_located(urlInput)).send_keys("https://the-internet.herokuapp.com")
    wait.until(EC.presence_of_element_located(go)).click()
    wait.until(EC.alert_is_present())
    alert=driver.switch_to.alert
    alert.accept()
    wait.until(EC.presence_of_element_located(clear)).click()
    contexts = driver.contexts
    print(contexts)
    webview_context = None
    for context in contexts:
        if 'WEBVIEW' in context:
            webview_context = context
            print(webview_context)
            break

    if webview_context:
        driver.switch_to.context(webview_context)
        print("Switched to WebView context:", webview_context)
    else:
        print("WebView context not found.")
    driver.get("https://the-internet.herokuapp.com/")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    wait.until(EC.presence_of_element_located(element)).click()
    username = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#username')))
    username.send_keys('tomsmith')
    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.send_keys('SuperSecretPassword!')
    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Logout'))).click()
    time.sleep(2)
    flash = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#flash')))
    print(flash.text)
    assert 'You logged out of the secure area!' in flash.text


except ValueError as e:
    print(f"Caught ValueError: {e}")
except KeyError as e:
    print(f"Caught KeyError: {e}")
except Exception as e:
    print(f"Caught exception: {e}")
