import time
from appium import webdriver
from os import path

from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

CURR_DIR=path.dirname(path.abspath(__file__))
APPIUM='http://localhost:4723'

CAPS = {
    'platformName': 'iOS',
    'platformVersion': '16.4',
    'deviceName': 'iPhone 14 Pro Max',
    'automationName': 'XCUITest',
    'bundleId': 'io.cloudgrey.the-app',
    'safariAllowPopups': False,

}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

webview=(MobileBy.ACCESSIBILITY_ID,'Webview Demo')
ioskeyboardhide=(MobileBy.XPATH,'(//XCUIElementTypeButton[@name="Return"])')
go=(MobileBy.XPATH,'(//XCUIElementTypeOther[@name="navigateBtn"])[2]')
clear=(MobileBy.XPATH,'(//XCUIElementTypeOther[@name="clearBtn"])[2]')
urlInput=(MobileBy.XPATH, '//XCUIElementTypeTextField[@name="urlInput"]')
ok=(MobileBy.ACCESSIBILITY_ID,'OK')
Vancouver=(MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="PlaceSummaryTitleLabel"])[1]')
stanley=(MobileBy.XPATH, '(//XCUIElementTypeOther[@name="VKPointFeature"])[4]')
element=(By.LINK_TEXT, "Form Authentication")


try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(webview)).click()
    contexts = driver.contexts
    print(contexts)
    wait.until(EC.presence_of_element_located(urlInput)).send_keys("https://the-internet.herokuapp.com")
    wait.until(EC.presence_of_element_located(go)).click()
    wait.until(EC.alert_is_present())
    driver.switch_to.alert
    wait.until(EC.presence_of_element_located(ok)).click()
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
        wait.until(EC.presence_of_element_located(ioskeyboardhide)).click()
        driver.switch_to.context(webview_context)
        print("Switched to WebView context:", webview_context)
    else:
        print("WebView context not found.")
    driver.get("https://the-internet.herokuapp.com/")

    #driver.execute_script("arguments[0].scrollIntoView();", element)
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

    '''print(driver.page_source)'''
    time.sleep(30)

except ValueError as e:
    print(f"Caught ValueError: {e}")
except KeyError as e:
    print(f"Caught KeyError: {e}")
except Exception as e:
    print(f"Caught exception: {e}")


finally:
    driver.quit()