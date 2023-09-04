import time
from appium import webdriver
from os import path
import math
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.mouse_button import MouseButton
from appium.webdriver.common.touch_action import TouchAction


#CURR_DIR=path.dirname(path.abspath(__file__))
#APP=path.join(CURR_DIR,"ApiDemos.apk")
#APPIUM='http://localhost:4723'
APPIUM='https://dev-us-pao-3.headspin.io:7005/v0/1f7e749a3421489fa8e618610b3e2740/wd/hub'

'''

CAPS = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'automationName': 'UiAutomator2',
    'app': APP,
}

'''
CAPS = {
    "deviceName": "SM-G781V",
    "udid": "RFCR7022DJL",
    "automationName": "uiautomator2",
    "appPackage": "io.appium.android.apis",
    "platformName": "android",
    'headspin:capture': True,
    "appActivity": ".ApiDemos"
}


driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

try:
    wait=WebDriverWait(driver,10)
    time.sleep(2)


    element=wait.until(EC.presence_of_element_located((MobileBy.XPATH,"//android.widget.TextView[@text='Graphics']")))
    element.click()
    screen_width = driver.get_window_size()['width']
    screen_height = driver.get_window_size()['height']
    radius = min(screen_width, screen_height) * 0.4
    center_x = screen_width / 2
    center_y = screen_height / 2
    move=center_y-(center_y/2)
    action = TouchAction(driver)

    while True:
        try:
            element=driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='FingerPaint']")
            element.click()
            break
        except :
            print("Test")
            action.press(x=center_x, y=center_y).wait(500).move_to(x=0, y=move).release().perform()

    print("Test 1")
    time.sleep(5)



    touch_action = TouchAction(driver)
    touch_action.press(x=center_x + radius, y=center_y)

    # Divide the circle into 360 equal parts and perform small movements along the circumference
    for angle in range(0, 380, 5):
        # Calculate the coordinates along the circumference based on the current angle

        x = center_x + int(radius * math.cos(math.radians(angle)))
        y = center_y + int(radius * math.sin(math.radians(angle)))
        touch_action.move_to(x=x, y=y)

    touch_action.release().perform()


    # Simulate drawing a circle using touch actions
    touch_action = TouchAction(driver)
    '''
    touch_action.press(x=center_x, y=center_y - radius) \
        .move_to(x=center_x + radius, y=center_y) \
        .move_to(x=center_x, y=center_y + radius) 
        .move_to(x=center_x - radius, y=center_y) \
        .move_to(x=center_x, y=center_y - radius) \
        .release() \
        .perform()
        
        '''

    touch_action = TouchAction(driver)
    touch_action.press(x=center_x-radius, y=center_y) \
          .move_to(x=center_x + radius, y=center_y) \
          .release() \
          .perform()

    touch_action = TouchAction(driver)
    touch_action.press(x=center_x, y=center_y - radius) \
        .move_to(x=center_x, y=center_y + radius) \
        .release() \
        .perform()

except ValueError as e:
    print(f"Caught ValueError: {e}")
except KeyError as e:
    print(f"Caught KeyError: {e}")
except Exception as e:
    print(f"Caught exception: {e}")




finally:
    driver.quit()