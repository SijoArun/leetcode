import time
from appium import webdriver
from os import path
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

CURR_DIR=path.dirname(path.abspath(__file__))
APPIUM='http://localhost:4723'

CAPS = {
    'platformName': 'iOS',
    'platformVersion': '16.4',
    'deviceName': 'iPhone 14 Pro Max',
    'automationName': 'XCUITest',
    'bundleId': 'com.apple.Maps',

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
searchmap=(MobileBy.XPATH, '//XCUIElementTypeSearchField[@name="MapsSearchTextField"]')
Vancouver=(MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="PlaceSummaryTitleLabel"])[1]')
stanley=(MobileBy.XPATH, '(//XCUIElementTypeOther[@name="VKPointFeature"])[4]')
assertmessage1="Invalid login credentials, please try again"
assertmessage2="You are logged in as alice"



try:
    wait=WebDriverWait(driver,10)

    wait.until(EC.presence_of_element_located(searchmap)).click()
    wait.until(EC.presence_of_element_located(searchmap)).send_keys("Vancouver, BC")
    ele=wait.until(EC.presence_of_element_located(Vancouver))
    ele.click()
    time.sleep(3)
    ele = wait.until(EC.presence_of_element_located(stanley))
    action = TouchAction(driver)
    print(ele.location)

    action.long_press(ele).wait(500).release().perform()
    action.press(x=376,y=99).release().perform()

    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    m_action = MultiAction(driver)


    # Zoom
    action1.long_press(x=148, y=236).move_to(x=10, y=50).wait(750).release()
    action2.long_press(x=148, y=236).move_to(x=-10, y=-50).wait(750).release()
    m_action.add(action1, action2)
    m_action.perform()
    time.sleep(20)

except ValueError as e:
    print(f"Caught ValueError: {e}")
except KeyError as e:
    print(f"Caught KeyError: {e}")
except Exception as e:
    print(f"Caught exception: {e}")


finally:
    driver.quit()