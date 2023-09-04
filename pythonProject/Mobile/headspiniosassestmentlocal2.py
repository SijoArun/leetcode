import time
from appium import webdriver
from os import path
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

APPIUM='https://dev-us-pao-0.headspin.io:7044/v0/1f7e749a3421489fa8e618610b3e2740/wd/hub'

CAPS = {
    "deviceName": "iPhone 11 Pro Max",
    "udid": "00008030-001535310E28802E",
    "automationName": "xcuitest",
    "platformVersion": "15.6",
    "platformName": "ios",
    "headspin:capture": "true",
    "bundleId": "com.apple.Maps"
}


driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

loginscreen=(MobileBy.ACCESSIBILITY_ID,'Login Screen')
username=(MobileBy.ACCESSIBILITY_ID, 'username')
password=(MobileBy.ACCESSIBILITY_ID, 'password')
loginbutton=(MobileBy.XPATH, '(//XCUIElementTypeOther[@name="loginBtn"])[2]')
message=(MobileBy.ACCESSIBILITY_ID, 'Invalid login credentials, please try again')
button=(MobileBy.ACCESSIBILITY_ID, 'OK')
continuefield2=(MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Continue"]')
searchmap=(MobileBy.XPATH, '//XCUIElementTypeSearchField[@name="Search Maps"]')
Vancouver=(MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="PlaceSummaryTitleLabel"])[1]')
stanley=(MobileBy.XPATH, '(//XCUIElementTypeOther[@name="Stanley Park"])')
assertmessage1="Invalid login credentials, please try again"
assertmessage2="You are logged in as alice"



try:
    wait=WebDriverWait(driver,10)
    wait.until(EC.presence_of_element_located(searchmap)).click()
    wait.until(EC.presence_of_element_located(searchmap)).send_keys("Vancouver, BC")
    ele=wait.until(EC.presence_of_element_located(Vancouver))
    ele.click()
    ele = wait.until(EC.presence_of_element_located(stanley))
    action = TouchAction(driver)
    print(ele.location)

    action.long_press(ele).wait(500).release().perform()
    action.press(x=376,y=99).release().perform()

    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    m_action = MultiAction(driver)


    # Zoom
    action1.long_press(x=142, y=200).move_to(x=10, y=50).wait(750).release()
    action2.long_press(x=142, y=200).move_to(x=-10, y=-50).wait(750).release()
    m_action.add(action1, action2)
    m_action.perform()
    time.sleep(2)


finally:
    driver.quit()